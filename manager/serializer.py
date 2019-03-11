from rest_framework import fields, serializers
from .models import *


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    teacher_1_view = TeacherSerializer(source='teacher_1',read_only=True)
    teacher_2_view = TeacherSerializer(source='teacher_2',read_only=True)
    class Meta:
        model = Class
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    student_cd = serializers.CharField(required=False)
    study_at_class_view = ClassSerializer(source='study_at_class',read_only=True)
    school_view = SchoolSerializer(source='school',read_only=True)

    class Meta:
        model = Student
        fields = ('id','student_cd','first_name','last_name','date_of_bidth','full_name','gender',
                'study_at_class','study_at_class_view','school_view', 'school',
                'current_class','current_school','eng_listening','eng_reading','eng_speaking','eng_writing',
                'gifted_skills','robotics_skills','robotics_month','student_phone','student_email',
                'note','father_name','father_dob','father_job','father_phone','father_email','mother_name',
                'mother_dob','mother_job','mother_phone','mother_email','address','has_other_siblings_study',
                'siblings_name','siblings_class')

class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.CharField(read_only=True)

    class Meta:
        model = UserBase
        fields = ('id','username','password','email','avatar',
            'birthday','avatar_url', 'first_name','last_name', 'full_name')
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'write_only': True},}

class UserWithTokenSerializer(UserSerializer):
    auth_token = serializers.CharField(read_only=True)
    
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('auth_token',)

