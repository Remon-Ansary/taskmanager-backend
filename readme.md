# Task Manager Backend

A Django REST Framework-based backend for the Task Manager application. It provides APIs for task management, including creating, retrieving, updating, deleting, and filtering tasks.

## Features

- Task Management: Create, view, edit, delete, and filter tasks
- Overdue Tasks: Retrieve tasks that are past their due date
- Pagination: Display tasks in paginated form
- Docker Support: Easy setup and deployment using Docker and Docker Compose
  

## Database Design and Sql Query: PostgreSQL

- You can find the database design in schema.txt file

## Nginx

- The Nginx configuration file is located in the nginxfile.txt file

## API Endpoints

### Tasks
- **List Tasks:** `GET /api/tasks/`
  - *Filters:* `status` (e.g., `/api/tasks/?status=Pending`)
- **Create Task:** `POST /api/tasks/`
- **Retrieve Task:** `GET /api/tasks/{id}/`
- **Update Task:** `PUT /api/tasks/{id}/`
- **Delete Task:** `DELETE /api/tasks/{id}/`
- **Overdue Tasks:** `GET /api/tasks/overdue/`

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- Gunicorn
- Docker

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


## Docker Setup

1. Ensure Docker and Docker Compose are installed

2. Build and Run Containers
   ```bash
   docker-compose up --build
   ```
3. Access the API at `http://localhost:8000/api/`
