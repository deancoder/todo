from django.db import models

# Create your models here.

TASK_STATUS = (
    ('CLOSE', 'CLOSE'),
    ('COMPLETED', 'COMPLETED'),
    ('OPEN', 'OPEN'),
    )


class TodayTask(models.Model):
    email = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    task_name = models.CharField(max_length = 100)
    task_time = models.TimeField()
    status = models.CharField(max_length = 40, choices=TASK_STATUS, default = "OPEN")

class User(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null = True)
    phone = models.IntegerField(default = 0)
