# Smart Library System Backend API

## Overview
The Smart Library System Backend API is a robust and scalable backend solution built with FastAPI and MongoDB. It is designed to manage library operations such as user management, book inventory, and loan tracking efficiently.

## Features
- **User Management**: Create, retrieve, and manage user information.
- **Book Management**: Add, retrieve, and manage book inventory, including available copies.
- **Loan Management**: Issue, track, and manage book loans.
- **Error Handling**: Graceful handling of invalid inputs and errors.

## Technology Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python.
- **Database**: [MongoDB](https://www.mongodb.com/) - A NoSQL database for storing and managing data.
- **ODM**: [Motor](https://motor.readthedocs.io/) - An asynchronous Python driver for MongoDB.
- **Package Manager**: [UV](https://uv-pypi.readthedocs.io/) - A Python package manager for managing dependencies and running projects.

## Prerequisites
- Python 3.12 or higher
- MongoDB instance (local or cloud-based)
- UV package manager installed globally:
  ```bash
  pip install uv
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastapi-mongodb-smart-library
   ```

2. Install dependencies using UV:
   ```bash
   uv install
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     MONGODB_URI=<your-mongodb-uri>
     DATABASE_NAME=smart_library
     DEBUG=True
     ```

## Running the Application
1. Start the FastAPI server using UV:
   ```bash
   uv run fastapi dev
   ```
   or
   ```bash
   uv run -m app.main
   ```

2. Access the API documentation:
   - Swagger UI: [http://localhost:3001/docs](http://localhost:3001/docs)
   - ReDoc: [http://localhost:3001/redoc](http://localhost:3001/redoc)

## Project Structure
```
fastapi-mongodb-smart-library/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── dal.py
│   │   ├── model.py
│   │   ├── routes.py
│   ├── books/
│   │   ├── __init__.py
│   │   ├── dal.py
│   │   ├── model.py
│   │   ├── routes.py
│   ├── loans/
│       ├── __init__.py
│       ├── dal.py
│       ├── model.py
│       ├── routes.py
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
```

## API Endpoints
### Users
- `POST /api/users/`: Create a new user.
- `GET /api/users/{user_id}`: Retrieve user details by ID.

### Books
- `POST /api/books/`: Add a new book.
- `GET /api/books/{book_id}`: Retrieve book details by ID.

### Loans
- `POST /api/loans/`: Issue a new loan.
- `GET /api/loans/{loan_id}`: Retrieve loan details by ID.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Motor](https://motor.readthedocs.io/)
- [UV](https://uv-pypi.readthedocs.io/)