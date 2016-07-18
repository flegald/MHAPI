"""REST Urls."""
from django.conf.urls import url
from RESTAPI import views


urlpatterns = [
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    url(r'^locations/(?P<name>[\w|\W]+)/$', views.LocationSingleView, name='location_single' ),
    url(r'^weapons/$', views.WeaponListView.as_view(), name='weapons'),
    url(r'^weaponsheavy/$', views.HeavyWeaponListView.as_view(), name='heavy weapons list'),
    url(r'^weapons/(?P<name>[\w|\W]+)/$', views.WeaponSingleView, name='weapon_single')	
]
