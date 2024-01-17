from django.db import models


class Task(models.Model):
    task_description = models.TextField()
    task_status = models.IntegerField(choices=[
        (0, 'Yet to Start'),
        (1, 'In Progress'),
        (2, 'Completed'),
    ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)