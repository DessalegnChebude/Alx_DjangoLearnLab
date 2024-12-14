# Social Media API

A Django REST API for a simple social media application allowing user registration, login, and profile management.

## Features

- User registration
- User login
- User profile retrieval
- Token-based authentication

## Technologies Used

- Django
- Django REST framework
- Django Rest Framework Authtoken
- SQLite (or any preferred database)
- Python 3.12.5

## Installation

### Prerequisites

- Python 3.12.5
- pip (Python package installer)
- http://127.0.0.1:8000/api/accounts/profile/        to see the user profile
- http://127.0.0.1:8000/api/accounts/login/           to login user
- http://127.0.0.1:8000/api/accounts/register/        to register user
# Social Media API

## Features
- User Registration
- Token-based Login
- User Profile Retrieval

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Endpoints
1. **Register**: `POST /api/accounts/register/`
2. **Login**: `POST /api/accounts/login/`
3. **Profile**: `GET /api/accounts/profile/` (requires token in header)

## Authentication
Use Token-based authentication for protected endpoints. Include the token in the `Authorization` header as:  
`Authorization: Token <your_token>`
