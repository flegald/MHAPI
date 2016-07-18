"""REST Urls."""
from django.conf.urls import url
from RESTAPI import views


urlpatterns = [
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    url(r'^locations/(?P<name>[\w|\W]+)/$', views.LocationSingleView, name='location_single' )	
]
