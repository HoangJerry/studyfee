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
    study_at_class = models.PositiveSmallIntegerField(_('study at class'))
    type_of_class = models.PositiveSmallIntegerField(_('type of class'))
    parent_first_name = models.CharField(_('parent first name'),max_length=200, null=True, blank=True)
    parent_last_name = models.CharField(_('parent last name'),max_length=200, null=True, blank=True)
    parent_phone = models.CharField(_('parent phone'),max_length=200, null=True, blank=True)
    parent_email = models.EmailField(_('parent email'))

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)