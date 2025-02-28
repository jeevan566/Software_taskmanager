from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('dashboard/', views.task_list, name='task_list'),  
    path('create/', views.create_task, name='create_task'), 
    path('register/', views.register, name='register'), 
    path('update/<int:pk>/', views.update_task, name='update_task'), 
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),  
]
