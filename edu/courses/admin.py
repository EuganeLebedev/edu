from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'owner']


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'course']
