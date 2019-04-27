from django.db import models


# Create your models here.
class Task(models.Model):
    task_desc = models.CharField(max_length=100)
