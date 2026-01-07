# Telegram Message Scheduler

Backend-focused Python project for scheduling and sending Telegram messages based on time triggers.

This project demonstrates working with **background jobs**, **external APIs**, **environment configuration**, and **advanced testing techniques** (monkeypatching time).

---

## Project Overview

Telegram Message Scheduler is a small backend service that:
- runs a background scheduler
- checks scheduled messages stored in JSON
- sends messages to a Telegram chat at the correct time
- exposes a minimal Flask endpoint for health checks (deployment-ready)

The project focuses on **backend behavior and reliability**, not UI.

---

## Tech Stack

- **Python**
- **Flask** (health check / service entry point)
- **APScheduler** (background scheduling)
- **Requests** (Telegram Bot API)
- **pytest** (unit testing)
- **monkeypatch** (time, file system, HTTP mocking)
- **dotenv** (environment configuration)

---

## Key Features

- Background job runs on a fixed interval
- Time-based message triggering (`YYYY-MM-DD HH:MM`)
- Messages stored in JSON (`messages_by_date.json`)
- Telegram Bot API integration
- Environment-based configuration (`BOT_TOKEN`, `CHAT_ID`)

---

## Project Structure

```text
telegram_message_scheduler/
├── main.py               # Flask app + scheduler startup
├── scheduler.py          # Background job logic
├── config.py             # Environment configuration
├── data/
│   └── messages_by_date.json
├── tests/
│   └── test_scheduler.py # Unit tests with monkeypatch
├── requirements.txt
├── Procfile
└── README.md
```

## Running locally
1. Clone the repository
2. Create .env file:
```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
python main.py
```

---
## Author
Created by Kateryna Babakova (https://github.com/katebabakova444) This project is part of my backend development journey.