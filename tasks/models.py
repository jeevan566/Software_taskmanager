from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    PROJECT_CHOICES = [
        ('RESEARCH', 'Research'),
        ('FINANCE', 'Finance'),
        ('MARKETING', 'Marketing'),
    ]
    
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='LOW')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    project = models.CharField(max_length=20, choices=PROJECT_CHOICES, default='RESEARCH')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link task to a user

    def __str__(self):
        return self.title
