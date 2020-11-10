from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, default=' ', primary_key=True, null=False)
    first_name = models.CharField (max_length=30, default=' ', null=True, blank=True)
    last_name = models.CharField (max_length=30, default=' ', null=True, blank=True)
    email = models.EmailField (max_length=50, default=' ', null=True, blank=True)
    phone = models.CharField (max_length=10, default=' ', null=True, blank=True)
    occupation = models.CharField (max_length=30, default=' ', null=True, blank=True)