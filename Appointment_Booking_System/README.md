# Appointment Booking System

## Overview
Create and view appointment bookings for a small office or college help desk.

## Main features
- Book appointments with name, date and time
- Validate required fields
- SQLite persistence
- Cancel bookings

## Technology
- Python 3.10 or newer
- Flask web framework
- SQLite database (created automatically on first run)
- HTML/CSS templates embedded in `app.py`

## Setup and run
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open the local URL shown in the terminal (usually `http://127.0.0.1:5000`).

## Database
SQLite data is stored in a local `.db` file in this folder. The file is created automatically when the app starts. Back up the database before deleting it.

## Academic submission checklist
- Add your name, roll number, course, department, and college details to the report.
- Take screenshots of the app running on your own computer.
- Test all main functions and document any bugs or limitations.
- Be ready to explain the code; follow your college's rules for AI-assisted work.

## Limitations and future scope
This is a functional educational prototype. Before real-world deployment, add authentication, input validation, CSRF protection, secure configuration, tests, and production hosting. Use only sample data for demonstrations.
