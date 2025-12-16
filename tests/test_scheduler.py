import json
from datetime import datetime
import scheduler
import builtins


def test_message_sent_when_time_matches(monkeypatch, tmp_path):
    fake_now = "2025-01-01 09:00"
    class FakeDatetime(datetime):
        @classmethod
        def now(cls):
            return datetime.strptime(fake_now, "%Y-%m-%d %H:%M")
    monkeypatch.setattr(scheduler, "datetime", FakeDatetime)
    messages = {
        fake_now: "Test scheduled message"
    }
    json_file = tmp_path / "messages_by_date.json"
    json_file.write_text(json.dumps(messages), encoding="utf-8")
    real_open = builtins.open

    monkeypatch.setattr(
        builtins,
        "open",
        lambda *args, **kwargs: real_open(json_file, *args[1:], **kwargs),
    )
    sent_requests = {}
    def fake_post(url, data):
        sent_requests["url"] = url
        sent_requests["data"] = data

        class FakeResponse:
            status_code = 200
            text = "OK"
        return FakeResponse
    monkeypatch.setattr(scheduler.requests, "post", fake_post)

    scheduler.send_scheduled_message()
    assert sent_requests["data"]["text"] == "Test scheduled message"

def test_message_not_sent_when_time_does_not_match(monkeypatch, tmp_path):
    fake_now = "2025-01-01 10:00"

    class FakeDatetime(datetime):
        @classmethod
        def now(cls):
            return datetime.strptime(fake_now, "%Y-%m-%d %H:%M")
    monkeypatch.setattr(scheduler, "datetime", FakeDatetime)
    messages = {
        "2025-01-01 09:00": "Should not be sent"
    }
    json_file = tmp_path / "messages_by_date.json"
    json_file.write_text(json.dumps(messages), encoding="utf-8")

    real_open = open
    monkeypatch.setattr(
        builtins,
        "open",
        lambda *args, **kwargs: real_open(json_file, *args[1:], **kwargs),
    )
    sent_requests = {}
    def fake_post(url, data):
        sent_requests["called"] = True
    monkeypatch.setattr(scheduler.requests, "post", fake_post)
    scheduler.send_scheduled_message()
    assert "called" not in sent_requests

