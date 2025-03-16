
This is a simple Task Management System built using Django that allows users to create, update, delete, and manage tasks with role-based permissions.

The following are its features:

Features
-User Authentication (Login, Register, Logout)
-Role-Based Access Control (Admin & Standard User)
-Task Management (Create, Update, Delete, View)
-Task Categorization (Projects, Priorities, Due Dates)
-Responsive UI (HTML, CSS, Bootstrap)
-Database Storage (SQLite)
-Deployment Ready (PythonAnywhere)

1. Super User
 user name: admin
 password: admin

2. Three Standard Users Login:

User Name: james
Password : userj12345

User Name: claire
Password : userc12345

User Name: Bob
Password : userb12345

I used following commands on on Local PC environment:
The given commands are essential Django management commands used to set up and run a Django project. Here’s what each command does in the given sequence:

py -3.10 manage.py makemigrations

This command creates migration files based on the changes detected in the models.
The number 1 indicates its position in the intended execution order.
py -3.10 manage.py migrate

Applies the migrations to the database, ensuring that the database schema matches the models.
The number 2 shows that it follows after generating migrations.
py -3.10 manage.py createsuperuser

Creates a superuser account to access the Django admin panel.
The number 3 suggests that it is done after applying migrations, as the user model needs to exist in the database.
py -3.10 manage.py runserver

Starts the Django development server, making the application accessible via http://127.0.0.1:8000/ by default.
The number 4 indicates that it is the final step after setting up the database and creating a superuser.




