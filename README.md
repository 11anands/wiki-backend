

# Cybervize Backend Coding Challenge

## Table of Contents

1. [Introduction](#Introduction)
2. [Installation](#Installation)

## Introduction

### Aim -

The aims to build a Search functionality with minimal UI to achieve the basic Search tasks. It fetches the data from an API providing objects of various information of several drugs. 

### Technology Used -

Programming Language: Python  
Framework: FastAPI

The reason of choosing FastAPI is because this functionality is just one feature, it needs to be lightweight without alot of processes hampering it. Hence FastAPI being a lightweight and a fast option for this usecase.

---

## Installation

The Repository contains 2 branches, React and Django as their names. React branch contains the react project while the Django branch contains the django part.

1. First step is to clone the project into a specific directory.

```bash
git clone https://github.com/11anands/react-django-task.git
```

2. The Project Structure should look like this:

```Project
|-- /alembic
|-- /app
    |-- /routers
|-- /constants
|-- /models
|-- /static
|-- /templates
|-- .env
|-- file.log
|-- alembic.ini
|-- docker-compose.yml
|-- Dockerfile
|-- json_to_postgres.py
|-- requirements.txt
```

4. Please go to the root directory of the project and run the following command to install the dependencies:

```docker
docker-compose build
```

3. Please go to the root directory of the project and run the following command to start the project:

```docker
docker-compose up -d
```

4. Please go to the root directory of the project and run the following command to make the migration file for Postgres database:

```docker
docker-compose run app alembic revision --autogenerate -m "New Migration"
```

5. Please go to the root directory of the project and run the following command to make the migrate the configuration to Postgres database:

```docker
docker-compose run app alembic upgrade head
```

6. If everything is successful, then the project should be accessible at http://127.0.0.1:8000/search/

---
