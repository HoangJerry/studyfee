from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import *
# Register your models here.
admin.site.unregister(auth.models.Group)

class UserBaseAdmin(UserAdmin):
    list_display = ('id','email','first_name','last_name','birthday')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Personal info'),
            {'fields': ('first_name', 'last_name', 'birthday','avatar',)}),
        (_('Permissions'), 
            {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), 
            {'fields': ('last_login', 'date_joined')}),
        )

    list_filter = ('is_staff', 'is_superuser')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','first_name','last_name','date_of_bidth',
                    'parent_first_name',
                    'parent_last_name','parent_phone','parent_email')

    filter_horizontal = ('parent',)

    
admin.site.register(UserBase, UserBaseAdmin)
admin.site.register(Student, StudentAdmin)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','date_of_bidth','phone','email','address')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = [field.name for field in School._meta.get_fields()]

@admin.register(ClassGroup)
@admin.register(Class)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
