from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import UserModel, StudentsGroupModel

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_student', 'is_teacher', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('course details'), {'fields': ('group_code', )}),
    )


admin.site.register(UserModel, CustomUserAdmin)

@admin.register(StudentsGroupModel)
class StudentsGroupAdmin(admin.ModelAdmin):
    list_display = ['group_code', 'start_date', 'get_student_counts']