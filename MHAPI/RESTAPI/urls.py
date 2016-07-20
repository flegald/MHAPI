"""REST Urls."""
from django.conf.urls import url
from RESTAPI import views


urlpatterns = [
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    url(r'^locations/(?P<name>[\w|\W]+)/$', views.LocationSingleView, name='location_single' ),
    url(r'^weapons/$', views.WeaponListView.as_view(), name='weapons'),
    url(r'^weaponsheavy/$', views.HeavyWeaponListView.as_view(), name='heavy weapons list'),
    url(r'^weapons/(?P<name>[\w|\W]+)/$', views.WeaponSingleView, name='weapon single'),
    url(r'^armor/$', views.ArmorListView.as_view(), name='armor'),
    url(r'^armorheavy/$', views.ArmorListViewHeavy.as_view(), name='Heavy Armor List'),
    url(r'^armor/(?P<name>[\w|\W]+)/$', views.ArmorSingleView, name='armor single'),
    url(r'^monsters/$', views.MonsterListView.as_view(), name='Monster List'),
    url(r'^monsters/(?P<name>[\w|\W]+)/$', views.MonsterSingleView.as_view(), name='Monster Single')
]
