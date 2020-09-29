from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class UserModel(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Phone number format must be +99999999')
    phone_number = models.CharField(validators=[phone_regex], max_length=18, blank=False, null=False, unique=True)
    #TODO Make many to many dependancy to group
    group_code = models.CharField(max_length=50, null=True, blank=True)
    is_student = models.BooleanField(default=True, blank=False, null=False)
    is_teacher = models.BooleanField(default=False, blank=False, null=False)