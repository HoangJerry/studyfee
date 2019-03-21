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
        self.queryset.filter(id__in=list_delete).delete()
        return Response(status=status.HTTP_200_OK,data={'detail':'delete success'})

import django_filters

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student    
        fields = {
            'student_cd': ['exact', 'contains'],
            'first_name': ['exact', 'contains'],
            'last_name': ['exact', 'contains'],
            'study_at_class': ['exact',],
            'school': ['exact',]
        }

class StudentList(generics.ListCreateAPIView, MultiDelete):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = StudentFilter

    def post(self, request, format=None):
        if request.data.get('list_delete'):
            return self.delete(request)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            student = serializer.create(serializer.validated_data)
            student.school.last_student_id+=1
            student.school.save()
            temp = f'{student.school.last_student_id:05}'
            student.student_cd = '{}-{}'.format(student.school.school_id,temp)
            student.save()
            return Response(StudentSerializer(student).data,status=status.HTTP_200_OK) 

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        previous_school = instance.school
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        student =  self.get_object()
        if not previous_school == student.school:
            student.school.last_student_id+=1
            student.school.save()
            temp = f'{student.school.last_student_id:05}'
            student.student_cd = '{}-{}'.format(student.school.school_id,temp)
            student.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



class ClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]
    paginator = None

class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]
    paginator = None