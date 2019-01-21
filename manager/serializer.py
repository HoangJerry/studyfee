from rest_framework import fields, serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.CharField(read_only=True)

    class Meta:
        model = UserBase
        fields = ('id','username','password','email','avatar',
            'birthday','avatar_url', 'first_name','last_name')
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'write_only': True},}

class UserWithTokenSerializer(UserSerializer):
    auth_token = serializers.CharField(read_only=True)
    
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('auth_token',)