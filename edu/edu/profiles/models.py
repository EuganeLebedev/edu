from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class StudentsGroupModel(models.Model):

    group_code = models.CharField(max_length=25, unique=True, blank=False, null=False, primary_key=True)
    start_date = models.DateField()
    is_finished = models.BooleanField(default=False, verbose_name='Обучение завершено')

    def __str__(self):
        return self.group_code

    class Meta:
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'


class UserModel(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Формат телефонного номера должен быть +99999999')
    phone_number = models.CharField(validators=[phone_regex], max_length=18, blank=False, null=False, unique=True)
    group_code = models.ManyToManyField(StudentsGroupModel, verbose_name='group')
    is_student = models.BooleanField(default=True, blank=False, null=False)
    is_teacher = models.BooleanField(default=False, blank=False, null=False)




