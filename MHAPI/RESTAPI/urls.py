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
    url(r'^monsters/(?P<name>[\w]+)/$', views.MonsterSingleView.as_view(), name='Monster Single'),
    url(r'^quests/$', views.QuestListView.as_view(), name='Quest List'),
    url(r'^quests/hub/(?P<hub>[\w]+)/$', views.QuestHubListView.as_view(), name='Quest Hub List'),
    url(r'^quests/hub/(?P<hub>[\w]+)/(?P<name>[\w|\W]+)/$', views.QuestSingleView.as_view(), name='Quest Single View'),
    url(r'^quests/monsters/(?P<monster>[\w|\W]+)/$', views.QuestsByMonster.as_view(), name='quests by monster'),
    url(r'^quests/stars/(?P<stars>[0-9]+)/$', views.QuestsByStars.as_view(), name="Quests By Stars"),
    url(r'^skills/$', views.SkillTreeList.as_view(), name='Skill Tree List'),
    url(r'^skills/(?P<name>[\w|\W]+)/$', views.SingleSkillTreeView.as_view(), name='Single Skill Tree'),
    url(r'^decorations/$', views.DecorationListView.as_view(), name="Decoration List View")
]
