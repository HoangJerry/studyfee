"""studyfee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from manager import urls as api_urls
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^docs/', include_docs_urls(title='Study fee API documentation')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL.replace(settings.SITE_URL, ''), document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL.replace(settings.SITE_URL, ''), document_root=settings.MEDIA_ROOT)
urlpatterns += url(r'^', TemplateView.as_view(template_name="index.html")),
