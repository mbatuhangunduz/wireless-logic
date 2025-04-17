# Wireless Logic FastAPI Project

## Project Structure


wireless-logic/
├── app/
│   ├── main.py            # FastAPI app instance
│   ├── models.py          # SQLAlchemy models
│   ├── database.py        # Database connection and session management
│   ├── router.py          # FastAPI router for endpoints
│   ├── crud.py            # CRUD operations
│   └── schemas.py         # Pydantic models (for request/response validation)
├── migrations/            # Alembic migrations
│   ├── env.py             # Alembic environment configuration
│   ├── versions/          # SQL migration scripts
│   ├── script.py.mako     # Template for generating migration scripts
└── alembic.ini        # Alembic configuration
├── .env                   # Environment variables (database URL, etc.)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration (optional)
├── docker-entrypoint.sh             
└── README.md              # Project documentation

This project is a REST API application built with FastAPI that integrates a PostgreSQL database and handles database migrations using Alembic. It provides basic CRUD operations for managing data. Below are the steps to set up, configure, and run the application.


## Prerequisites

Make sure you have the following installed:

- Python 3.12 (or higher)
- PostgreSQL (local or remote)
- Virtual environment manager (e.g., `venv`)

## Installation Steps

### 1. Create a Virtual Environment

Create a virtual environment for your project:

python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Set Up .env File
Create a .env file in the root directory of your project to store environment variables such as your database URL.

Example .env file:

POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db_name>
HOST=<host>

### 4. Database Setup

a. Create the Database
Before running migrations, ensure your PostgreSQL database is created:

psql -U postgres
CREATE DATABASE dbname;

b. Set Up Alembic for Migrations
Initialize Alembic in your project:

alembic init migrations

This creates a migrations/ folder containing the necessary configuration files.

In the alembic.ini file, configure the connection string to point to your PostgreSQL database:

sqlalchemy.url = postgresql://user:password@localhost/dbname

In migrations/env.py, ensure your models are imported to track them for migrations:

from app import models
target_metadata = models.Base.metadata

### 5.Generate and Apply Migrations
a. Generate Migrations
Generate the migration script:

alembic revision --autogenerate -m "First migration"

b. Apply Migrations
Apply the migration script:

alembic upgrade head

b. Output Migrations as SQL Files
To generate migration scripts as plain SQL files:

alembic upgrade head --sql > migrations/versions/migration_name.sql


### 6. To Run with Uvicorn

Start the FastAPI application using Uvicorn:

uvicorn app.main:app --reload

PLEASE NOTE: When you start the application with Uvicorn, you must set the HOST field in the .env file to "localhost" or comment out the HOST field.

### 7. To Run with Docker

After you started the docker and be sure about docker is running then you can simply
run these commands :

docker-compose build<br/>
then<br/>
docker-compose up<br/>
in the first time you start the project.


### 8. Swagger Documentation

You can access the Swagger documentation after running the application at: [http://localhost:8000/docs]
You can also access the Postman collection by importing the postman.json file through your own Postman application.


### 9. Test Application 

This project includes automated tests located in the tests folder. Specifically, the file test_api.py contains tests for the FastAPI endpoints, ensuring that the API functions as expected. You can run the tests using pytest:

PLEASE NOTE: When you test the application with pytest, you must set the HOST field in the .env file to "localhost" or comment out the HOST field.

pytest



### NOTES

- Currently, since the application is prepared over only a single db model, sql relations were not used. As I stated in the comments in the models.py file, relations such as one-to-many or many-to-many should be used in a more comprehensive application.

- In a more comprehensive study, operations such as migration with Alembic and testing the application with pytest can be done automatically every time the project is started by dockerizing it.

- In order to keep database hosts dynamically in Docker and Uvicorn environments, a more suitable production environment or a local computer can be determined and the host can be defined.