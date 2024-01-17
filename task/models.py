from django.db import models


class Task(models.Model):

    STATUS_CHOICES = [
        (0, 'Yet to Start'),
        (1, 'In Progress'),
        (2, 'Completed'),
    ]

    task_description = models.TextField()
    task_status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
