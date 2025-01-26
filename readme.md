# Task Manager Backend

A Django REST Framework-based backend for the Task Manager application. It provides APIs for user authentication and task management, including creating, retrieving, updating, deleting, and filtering tasks.

## Features

- User Authentication: Register, login, and logout users
- Task Management: Create, view, edit, delete, and filter tasks
- Overdue Tasks: Retrieve tasks that are past their due date
- Docker Support: Easy setup and deployment using Docker and Docker Compose

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- Gunicorn
- Docker
- Docker Compose
- Nginx (optional)

## Prerequisites

- Python 3.8+
- pip
- PostgreSQL (if not using Docker)
- Docker and Docker Compose (optional)
- Git

## Installation

### Local Setup

1. Clone the Repository
   ```bash
 
   cd taskmanager
   ```

2. Create a Virtual Environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. Install Dependencies
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Apply Migrations
   ```bash
   python manage.py migrate
   ```

5. Run the Server
   ```bash
   python manage.py runserver
   ```
   Access the API at `http://localhost:8000/api/`

## API Endpoints
### Tasks
- **List Tasks:** `GET /api/tasks/`
  - *Filters:* `status` (e.g., `/api/tasks/?status=Pending`)
- **Create Task:** `POST /api/tasks/`
- **Retrieve Task:** `GET /api/tasks/{id}/`
- **Update Task:** `PUT /api/tasks/{id}/`
- **Delete Task:** `DELETE /api/tasks/{id}/`
- **Overdue Tasks:** `GET /api/tasks/overdue/`

## Docker Setup

1. Ensure Docker and Docker Compose are installed

2. Build and Run Containers
   ```bash
   docker-compose up --build
   ```
3. Access the API at `http://localhost:8000/api/`
