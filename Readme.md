# Task Management System

A Django-based task management application featurs a role-based permissions and user-based task management functionality.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-jeevanrai.pythonanywhere.com-blue)](https://jeevanrai.pythonanywhere.com/)

## Features

* User Authentication (Login, Register, Logout)
* Role-Based Access Control (Admin & Standard User)
* Task Management (Create, Update, Delete, View)
* Task Categorization (Projects, Priorities, Due Dates)
* Responsive UI (HTML, CSS, Bootstrap)
* Database Storage (SQLite)
* Deployment Ready (PythonAnywhere)

## Test Credentials

### Super User
```markdown
Username: admin
Password: admin
```

### Standard Users
```markdown
User 1:
Username: james
Password: userj12345

User 2:
Username: claire
Password: userc12345

User 3:
Username: Bob
Password: userb12345
```

## Setup Instructions

To set up the project locally, execute these commands in sequence:

### Step 1: Create Database Migrations
```bash
py -3.10 manage.py makemigrations
```
This command generates migration files based on model changes detected in your Django application.

### Step 2: Apply Migrations
```bash
py -3.10 manage.py migrate
```
Applies migrations to ensure your database schema matches your models.

### Step 3: Create Admin Account
```bash
py -3.10 manage.py createsuperuser
```
Sets up a superuser account for Django admin panel access.

### Step 4: Start Development Server
```bash
py -3.10 manage.py runserver
```
Launches the development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


Thank you.
