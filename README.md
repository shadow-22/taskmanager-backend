### Backend README (Django)

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
    mkdir backend
    cd backend
    git clone https://github.com/shadow-22/taskmanager-backend.git
    cd taskmanager-backend

2. **Install dependencies:**
    ```bash
    pipenv install

3. **Activate the virtual environment:**
    ```bash
    pipenv shell

4. **Run database migrations:**
    ```bash
    cd taskmanager
    python manage.py migrate

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser

6. **Start the development server:**
    ```bash
    python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/

7. **API Endpoints:**

    User Registration: POST /api/register/

    User Login: POST /api/login/

    Task List and Create: GET/POST /api/tasks/

    Task Update and Delete: PUT/DELETE /api/tasks/<id>/

8. **Pagination:**
    GET /api/tasks/?page=<page_number>
    
    Tasks are paginated with the page parameter.

9. **Filtering:**
    GET /api/tasks/?is_completed=true (or false)

