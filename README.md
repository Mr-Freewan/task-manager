# Task Manager

Simple and flexible task management web application

[![Actions Status](https://github.com/Mr-Freewan/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Mr-Freewan/python-project-52/actions)
[![Actions Status](https://github.com/Mr-Freewan/python-project-52/actions/workflows/test-lint-check.yml/badge.svg)](https://github.com/Mr-Freewan/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/72817d69c4c9d12655a9/maintainability)](https://codeclimate.com/github/Mr-Freewan/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/72817d69c4c9d12655a9/test_coverage)](https://codeclimate.com/github/Mr-Freewan/python-project-52/test_coverage)

### Description

A task management web application built with Python
and [Django](https://www.djangoproject.com/) framework. It allows you to set
tasks, assign executors and change their statuses. Registration and
authentication are required to work with the system.

Demo app is [HERE](https://task-manager-ieeg.onrender.com/) (Requests can be delayed about 50 seconds or more).

### Features

* [x] Set tasks;
* [x] Assign executors;
* [x] Change task status;
* [x] Set multiple tasks labels;
* [x] Filter the tasks displayed by executors, author, labels and status;
* [x] User authentication and registration;

### Links

This project was built using these tools:

| Tool                                                            | Description                                                                                                  |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [Dgango](https://www.djangoproject.com/)                        | "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design." |
| [Poetry](https://python-poetry.org/)                            | "Python dependency management and packaging made easy"                                                       |
| [Flake8](https://flake8.pycqa.org/)                             | "Your tool for style guide enforcement"                                                                      | 
| [Bootstrap](https://getbootstrap.com/)                          | "Powerful, extensible, and feature-packed frontend toolkit."                                                 |   
| [PostgreSQL](https://www.postgresql.org/)                       | "The World's Most Advanced Open Source Relational Database"                                                  |
| [Gunicorn](https://gunicorn.org/)                               | "WSGI HTTP Server for UNIX"                                                                                  | 
| [Whitenoise](http://whitenoise.evans.io/en/latest/)             | "Radically simplified static file serving for Python web apps"                                                                                  | 

---

## Installation

### Important!

* [X] The project uses the Poetry dependency manager. Install it
  with [official instruction](https://python-poetry.org/docs/#installation).
* [X] You need to install the Postgre SQL
  from [official website](https://www.postgresql.org/download/) or use SQLite.

### Application

Clone the project:

    git clone https://github.com/Mr-Freewan/python-project-52.git && cd python-project-52

Then install dependencies:

    make install

Create .env file in the root folder and add following variables:

    SECRET_KEY = '{your secret key}' // Django secret key

If you want to use PostgreSQL:
    
    DATABASE_URL = postgresql://{provider}://{user}:{password}@{host}:{port}/{db}

If you choose to use SQLite, do not add DATABASE_URL variable.

If you want to crease superuser automatically:

    DJANGO_SUPERUSER_USERNAME = '{name}'
    DJANGO_SUPERUSER_PASSWORD = '{password}'
    DJANGO_SUPERUSER_EMAIL = '{email}' // for notifications

For PAAS (Render, Railway, etc):

    PAAS_HOSTNAME = '{hostname}'

For [Rollbar](https://rollbar.com) errors tracking:

    ROLLBAR_TOKEN = '{token}'

To create the tables in the database, start the migration process:
  
    make migrate

If you want create superuser:

    make create_superuser

## Usage

Start the gunicorn server by running (UNIX):

    make start

The server url will be at terminal, for example http://0.0.0.0:8000.

Or start the development mode:

    make dev

The server url will be at terminal, for example http://127.0.0.1:8000.

### Available Actions:

- **_Registration_** — First, you need to register in the application using the registration form provided;
- **_Authentication_** — To view the list of tasks and create new ones, you need to log in using the information from the registration form;
- **_Users_** — You can see the list of all registered users on the corresponding page. It is available without authorization. You can change or delete information only about yourself. If a user is the author or performer of a task, it cannot be deleted;
- **_Statuses_** — You can view, add, update, and delete task statuses if you are logged in. Statuses corresponding to any tasks cannot be deleted;
- **_Tasks_** — You can view, add, and update tasks if you are logged in. Only the task creator can delete tasks. You can also filter tasks on the corresponding page with specified statuses, performers, and labels;
- **_Labels_** — You can view, add, update, and delete task labels if you are logged in. Labels matching any tasks cannot be deleted.

---
