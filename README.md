### Backend README (Django)

```markdown
# Task Manager - Backend (Django REST API)

This is the backend part of the **Task Manager** app, built using **Django** and **Django REST Framework**. It provides APIs for managing tasks, user authentication (registration and login), and pagination support.

## Features

- User registration and authentication (token-based).
- Task management (create, update, delete, and list tasks).
- Pagination and filtering support.
- Built-in security and permissions (only authenticated users can access tasks).

## Prerequisites

- Python 3.8 or higher
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for environment management)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone <repo-url>
    cd <repo-directory>/backend

2. **Install dependencies**
    pipenv install

3. **Activate the virtual environment**
    pipenv shell

4. **Run database migrations**
    python manage.py migrate

5. **Create a superuser**
    python manage.py createsuperuser

6. **Start the development server**
    python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/

## API Endpoints
User Registration: POST /api/register/
User Login: POST /api/login/
Task List and Create: GET/POST /api/tasks/
Task Update and Delete: PUT/DELETE /api/tasks/<id>/
Pagination and Filtering
The task listing API supports pagination and filtering:

## Pagination
GET /api/tasks/?page=<page_number>
Tasks are paginated with the page parameter.

## Filtering
GET /api/tasks/?is_completed=true (or false)

