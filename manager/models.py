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
    CONST_GENDER_MALE = 0
    CONST_GENDER_FEMALE = 10
    CONST_GENDER_OTHER = 20

    CONST_GENDER = (
        (CONST_GENDER_MALE, _('Male')),
        (CONST_GENDER_FEMALE, _('Female')),
        (CONST_GENDER_OTHER, _('Other')),
    )

    student_cd = models.CharField(_('student id'), max_length=200,null=True, blank=True)
    first_name = models.CharField(_('first name'),max_length=25)
    last_name = models.CharField(_('last name'),max_length=10)
    gender = models.PositiveSmallIntegerField(_('gender'), choices=CONST_GENDER,
                                        default=CONST_GENDER_OTHER)
    date_of_bidth = models.DateField(_('date of bidth'), null=True, blank=True)
    current_class = models.CharField(_('current class'),max_length=10, null=True, blank=True)
    current_school = models.CharField(_('current school'),max_length=10, null=True, blank=True)
    eng_listening = models.FloatField(_('english listening'), null=True, blank=True)
    eng_reading = models.FloatField(_('english reading'), null=True, blank=True)
    eng_speaking = models.FloatField(_('english speaking'), null=True, blank=True)
    eng_writing = models.FloatField(_('english writing'), null=True, blank=True)

    gifted_skills = models.CharField(_('gifted skill'),max_length=200, null=True, blank=True)
    robotics_skills = models.CharField(_('robotics skills'),max_length=200, null=True, blank=True)
    robotics_month = models.CharField(_('robotics month'),max_length=200, null=True, blank=True)
    student_phone = models.CharField(_('student phone'),max_length=10, null=True, blank=True)
    student_email = models.EmailField(_('student email'),null=True, blank=True)

    study_at_class = models.ForeignKey("Class", on_delete=models.CASCADE)
    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="students")

    note = models.CharField(_('note'),max_length=200, null=True, blank=True)
    # family infor
    father_name = models.CharField(_('father name'),max_length=200, null=True, blank=True)
    father_dob = models.DateField(_('father\'s birthday'), null=True, blank=True)
    father_job = models.CharField(_('father job'),max_length=200, null=True, blank=True)
    father_phone = models.CharField(_('father phone'),max_length=200, null=True, blank=True)
    father_email = models.EmailField(_('father email'), null=True, blank=True)

    mother_name = models.CharField(_('mother name'),max_length=200, null=True, blank=True)
    mother_dob = models.DateField(_('mother\'s birthday'), null=True, blank=True)
    mother_job = models.CharField(_('mother job'),max_length=200, null=True, blank=True)
    mother_phone = models.CharField(_('mother phone'),max_length=200, null=True, blank=True)
    mother_email = models.EmailField(_('mother email'), null=True, blank=True)

    address = models.CharField(_('address'),max_length=200, null=True, blank=True)

    has_other_siblings_study = models.BooleanField(default=False)
    siblings_name = models.CharField(_('siblings name'),max_length=200, null=True, blank=True)
    siblings_class = models.CharField(_('siblings class'),max_length=200, null=True, blank=True)

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
    start_date = models.DateField(_('start date'), null=True, blank=True)
    end_date = models.DateField(_('end date'), null=True, blank=True)
    place = models.CharField(_('place'),max_length=200, null=True, blank=True)
    teacher_1 = models.ForeignKey("Teacher", related_name='teacher_1', on_delete=models.CASCADE)
    teacher_2 = models.ForeignKey("Teacher", related_name='teacher_2', on_delete=models.CASCADE)
    note = models.CharField(_('note'),max_length=200, null=True, blank=True)

    def __str__(self):
        return self.class_id


class Teacher(models.Model):
    teacher_id = models.CharField(_('teacher id'),max_length=200, null=True, blank=True)
    first_name = models.CharField(_('first name'),max_length=25, null=True, blank=True)
    last_name = models.CharField(_('last name'),max_length=10, null=True, blank=True)
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
    school_id = models.CharField(_('school id'), unique=True, max_length=200)
    name = models.CharField(_('name'),max_length=200, null=True, blank=True)
    president = models.CharField(_('president'),max_length=200, null=True, blank=True)
    date_of_bidth = models.DateField(_('date of bidth'))
    phone = models.CharField(_('phone'),max_length=200, null=True, blank=True)
    email = models.EmailField(_('email'))
    address = models.CharField(_('address'),max_length=200, null=True, blank=True)
    note = models.CharField(_('note'),max_length=200, null=True, blank=True)
    last_student_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name if self.name else "Object School"
