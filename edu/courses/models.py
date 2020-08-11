from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CourseAbstractModel(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Subject(CourseAbstractModel):
    pass

class Course(CourseAbstractModel):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    overview = RichTextField(blank=True, null=True)


class Module(CourseAbstractModel):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
