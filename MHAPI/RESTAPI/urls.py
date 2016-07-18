"""REST Urls."""
from django.conf.urls import url
from RESTAPI import views


urlpatterns = [
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    #url(r'^locations/$', LocationListView)
]
