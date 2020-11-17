from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.
from profiles.models import UserModel

class CourseAbstractModel(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Subject(CourseAbstractModel):
    pass

class Course(CourseAbstractModel):

    title_image = models.ImageField(upload_to='courses_titles', default='courses_titles/empty.png')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    overview = RichTextUploadingField(blank=True, null=True)



class Module(CourseAbstractModel):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)


class ModuleTest(CourseAbstractModel):

    module = models.OneToOneField(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):

    module_test = models.ForeignKey(ModuleTest, on_delete=models.CASCADE)
    question = models.CharField(max_length=256, null=False, blank=False)

    def __repr__(self):
        return self.question

    def __str__(self):
        return self.question

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256, blank=False, null=False)
    is_correct = models.BooleanField(default=False)


class StudentAnswer(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

