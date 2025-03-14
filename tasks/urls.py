##Jeevan Project Material##
from django.urls import path  # Import the path function to define URL patterns
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in authentication views
from . import views  # Import views from the current app

# Define URL patterns for the task management application
urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),  
    # Login page using Django's built-in authentication system with a custom template
    
    path('logout/', LogoutView.as_view(), name='logout'),  
    # Logout functionality using Django's built-in LogoutView
    
    path('dashboard/', views.task_list, name='task_list'),  
    # Route to display the list of tasks on the dashboard
    
    path('create/', views.create_task, name='create_task'),  
    # Route to create a new task
    
    path('register/', views.register, name='register'),  
    # Route for user registration
    
    path('update/<int:pk>/', views.update_task, name='update_task'),  
    # Route to update a task; expects a primary key (pk) as an integer in the URL
    
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),  
    # Route to delete a specific task based on its primary key (pk)
]
