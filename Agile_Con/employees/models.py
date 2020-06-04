from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class EmployeeAdmin(AbstractUser):
    username = models.CharField(unique= True, max_length=50, blank=False, null=False, default=' ')
    email = models.EmailField(max_length=100, default=' ')
    cell_phone = models.CharField(max_length=50, default='(402)000-0000')
    role = models.CharField(max_length=50, blank=False)