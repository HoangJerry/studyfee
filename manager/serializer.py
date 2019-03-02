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
    study_at_class_view = ClassSerializer(source='study_at_class',read_only=True)
    school_view = SchoolSerializer(source='school',read_only=True)

    class Meta:
        model = Student
        fields = ('id','student_id','first_name','last_name','date_of_bidth','study_at_class',
                'study_at_class_view','school_view',
                'school','parent_first_name','parent_last_name','parent_phone',
                'parent_email','full_name')

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

