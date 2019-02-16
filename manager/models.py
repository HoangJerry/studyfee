from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
# Create your models here.

class UserBase(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    birthday = models.DateField(null=True, blank=False)
    avatar = models.ImageField(help_text=_('Picture shall be squared, max 640*640, 500k'), upload_to='avatars',
                                 null=True, blank=True)

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name,self.last_name)

@receiver(post_save, sender=UserBase)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Student(models.Model):
    student_id = models.CharField(_('student id'), unique=True, max_length=200)
    first_name = models.CharField(_('first name'),max_length=200, null=True, blank=True)
    last_name = models.CharField(_('last name'),max_length=200, null=True, blank=True)
    date_of_bidth = models.DateField(_('date of bidth'))
    study_at_class = models.ForeignKey("Class", on_delete=models.CASCADE, null=True, blank=True)
    parent_first_name = models.CharField(_('parent first name'),max_length=200, null=True, blank=True)
    parent_last_name = models.CharField(_('parent last name'),max_length=200, null=True, blank=True)
    parent_phone = models.CharField(_('parent phone'),max_length=200, null=True, blank=True)
    parent_email = models.EmailField(_('parent email'))
    parent = models.ManyToManyField("Parent")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

class Parent(models.Model):
    first_name = models.CharField(_('first name'),max_length=200, null=True, blank=True)
    last_name = models.CharField(_('last name'),max_length=200, null=True, blank=True)
    date_of_bidth = models.DateField(_('date of bidth'))
    phone = models.CharField(_('parent phone'),max_length=200, null=True, blank=True)
    email = models.EmailField(_('parent email'))
    address = models.CharField(_('address'),max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

class ClassGroup(models.Model):
    class_group_id = models.CharField(_('class_group_id'),max_length=200, null=True, blank=True)
    name = models.CharField(_('name'),max_length=200, null=True, blank=True)
    note = models.CharField(_('note'),max_length=200, null=True, blank=True)


    def __str__(self):
        return self.class_group_id

class Class(models.Model):
    class_id = models.CharField(_('class id'),max_length=200, null=True, blank=True)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    name = models.CharField(_('name'),max_length=200, null=True, blank=True)
    estimate_start_date = models.DateField(_('estimate start date'))
    estimate_end_date = models.DateField(_('estimate end date'))
    start_date = models.CharField(_('start date'),max_length=200, null=True, blank=True)
    end_date = models.CharField(_('end date'),max_length=200, null=True, blank=True)
    place = models.CharField(_('note'),max_length=200, null=True, blank=True)
    teacher_1 = models.ForeignKey("Teacher", related_name='teacher_1', on_delete=models.CASCADE)
    teacher_2 = models.ForeignKey("Teacher", related_name='teacher_2', on_delete=models.CASCADE)
    note = models.CharField(_('note'),max_length=200, null=True, blank=True)

    def __str__(self):
        return self.class_id


class Teacher(models.Model):
    teacher_id = models.CharField(_('teacher id'),max_length=200, null=True, blank=True)
    first_name = models.CharField(_('first name'),max_length=200, null=True, blank=True)
    last_name = models.CharField(_('last name'),max_length=200, null=True, blank=True)
    phone = models.CharField(_('phone'),max_length=200, null=True, blank=True)
    email = models.EmailField(_('email'))
    address = models.CharField(_('address'),max_length=200, null=True, blank=True)
    note = models.CharField(_('note'),max_length=200, null=True, blank=True)


    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

class School(models.Model):
    name = models.CharField(_('name'),max_length=200, null=True, blank=True)
    president = models.CharField(_('president'),max_length=200, null=True, blank=True)
    date_of_bidth = models.DateField(_('date of bidth'))
    phone = models.CharField(_('phone'),max_length=200, null=True, blank=True)
    email = models.EmailField(_('email'))
    address = models.CharField(_('address'),max_length=200, null=True, blank=True)
    note = models.CharField(_('note'),max_length=200, null=True, blank=True)
