from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    position = models.CharField(max_length=64)
    probation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} ({self.position})"


class Order(models.Model):
    task_id = models.IntegerField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    def __str__(self):
        return f"{self.task_id} - {self.name}"
