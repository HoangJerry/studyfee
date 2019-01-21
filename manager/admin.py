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
                    'study_at_class','type_of_class','parent_first_name',
                    'parent_last_name','parent_phone','parent_email')
    
admin.site.register(UserBase, UserBaseAdmin)
admin.site.register(Student, StudentAdmin)