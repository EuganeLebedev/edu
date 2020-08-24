from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'owner']
    prepopulated_fields = {'slug': ('title', ) }


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    prepopulated_fields = {'slug': ('title', ) }


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'course']
    prepopulated_fields = {'slug': ('title', ) }


@admin.register(models.ModuleTest)
class ModuleTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'module']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'module_test']


@admin.register(models.Answer)
class AnsverAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']