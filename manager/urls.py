from django.conf.urls import include, url
from . import models
from . import api as api_views

urlpatterns = [
    url(r'^student/$', api_views.StudentList.as_view(), name='student-list'),
    url(r'^student/(?P<pk>[0-9]+)/$', api_views.StudentDetail.as_view(), name='student-detail'),
    url(r'^user/me/$', api_views.UserProfile.as_view(), name='user-me'),

]