from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    identification = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.email