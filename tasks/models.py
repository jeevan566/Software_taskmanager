##Jeevan Project Material##
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    # priority choices
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    # project categories
    PROJECT_CHOICES = [
        ('RESEARCH', 'Research'),
        ('FINANCE', 'Finance'),
        ('MARKETING', 'Marketing'),
    ]

    
    title = models.CharField(max_length=255) # link to title
    name = models.CharField(max_length=255) # link to name
    description = models.TextField() # task desciprtion field
    due_date = models.DateField() # due date field
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='LOW') # priority field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING') # status field
    project = models.CharField(max_length=20, choices=PROJECT_CHOICES, default='RESEARCH') # task category field
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link task to a user

    def __str__(self):
        return self.title
