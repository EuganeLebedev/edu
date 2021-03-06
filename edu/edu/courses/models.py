from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# from django.template.defaultfilters import slugify
from django.db.models import Prefetch
from slugify import slugify
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={'pk': self.pk})

    def get_module_set(self):
        return self.module_set





class Module(CourseAbstractModel):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('courses:module_detail', kwargs={'pk': self.pk})


class ModuleTest(CourseAbstractModel):

    module = models.OneToOneField(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('courses:module_test', kwargs={'pk': self.pk})

    def get_questions(self):
        return ModuleTest.objects.prefetch_related("question_set").get(pk=self.pk).question_set.all()
        # return self.question_set.all()


class Question(models.Model):

    module_test = models.ForeignKey(ModuleTest, on_delete=models.CASCADE)
    question = RichTextUploadingField(max_length=256, null=False, blank=False)

    def __repr__(self):
        return self.question

    def __str__(self):
        return f"{self.id} {self.question}"

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256, blank=False, null=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class StudentAnswer(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "question"]

class StudentModuleTestStatus(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    module_test = models.ForeignKey(ModuleTest, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)

    def str(self):
        return f"{self.user.username} is {self.passed}"

