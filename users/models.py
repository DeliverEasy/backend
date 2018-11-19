from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'mayorista'),
        (2, 'minorista'),
        (3, 'empleado'),
        (4, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Mayorista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Minorista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
