# To-Do List API

## Description
This is a To-Do List API built with Python 3.9+,  FastAPI framework, SQLAlchemy ORM, and MySQL/SQLite, providing CRUD operations for managing to-do items and user authentication. The API uses OAuth2 for authentication and JWT (JSON Web Tokens) for securing API endpoints. It is structured into routers for different functionalities and utility modules for common operations.


### Project Structure

The project structure is organized as follows:


    todo/
    ├── routers/
    |   ├── authentication.py   # Router for user authentication
    |   ├──  todo.py            # Router for to-do operations
    │   └── user.py             # Router for user operations
    ├── utils/
    │   ├── todo.py             # Utility functions for to-do operations
    │   └── user.py             # Utility functions for user operations
    ├── database.py             # Database configuration (MySQL or SQLite)
    ├── hashing.py              # Hashing utilities
    ├── main.py                 # Main FastAPI application
    ├── models.py               # SQLAlchemy models
    ├── oauth2.py               # OAuth2 authentication
    ├── schemas.py              # Pydantic schemas
    ├── token.py                # JWT token utilities
    requirements.txt            # List of project dependencies

## Installation
1. Install the 3.9+ version of Python from <https://www.python.org/>.
2. Clone this repository.
3. Navigate to the directory that you cloned this repository to, then run:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
4. Start the FastApi Server using following command
```
uvicorn todo.main:app --reload
```
### Api Documentation
Access the API documentation at <http://localhost:8000/docs> in your web browser.
