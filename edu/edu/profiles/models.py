from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserModel(AbstractUser):
    #TODO Make many to many dependancy to group
    group_code = models.CharField(max_length=50, null=True, blank=True)