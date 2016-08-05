"""MHAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from MHAPI.views import show_image
from django.conf import settings
from django.conf.urls import patterns
from .views import landing



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', landing),
    url(r'^media/(?P<map_img>[\w|\W]+)/$', show_image, name='show_image'),

    #API
    url(r'^api/', include('RESTAPI.urls', namespace='MHGen API'))
]

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )