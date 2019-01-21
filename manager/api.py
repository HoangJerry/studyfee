from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, exceptions, permissions, viewsets, mixins
from .serializer import *
from .models import *
from . import api_utils
from datetime import datetime

from django.contrib.auth import authenticate

# User login and get their profile
class UserProfile(generics.GenericAPIView):
    serializer_class = UserWithTokenSerializer

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        user = None

        if request.user.is_authenticated:
            user = request.user
        elif email and password:
            user = authenticate(username=email, password=password)
        if not user:
            raise api_utils.BadRequest("INVALID_PROFILE")

        if type(user) == UserBase:
            user.last_login = datetime.now()
            user.save()
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        raise api_utils.BadRequest("INVALID_PROFILE")

class MultiDelete():
    def delete(self, request):
    	list_delete = request.data.get('list_delete')
    	self.queryset.filter(id__in=list_delete)
    	return Response(status=status.HTTP_200_OK)

class StudentList(generics.ListCreateAPIView, MultiDelete):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer