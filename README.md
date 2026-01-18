# Task Manager API

> 📅 Developed in 2023 | Migrated to GitHub 2025

REST API for task management with Flask and SQLAlchemy.

## Technologies

- Python 3.9
- Flask 2.3
- SQLAlchemy
- SQLite

## Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
flask run
```

API available at `http://localhost:5000`

## Endpoints

- GET /api/tasks - List all tasks
- GET /api/tasks/{id} - Get task by ID
- POST /api/tasks - Create new task
- PUT /api/tasks/{id} - Update task
- DELETE /api/tasks/{id} - Delete task
- PATCH /api/tasks/{id}/complete - Mark task as completed
