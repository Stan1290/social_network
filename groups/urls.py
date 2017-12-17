from django.conf.urls import url
from . import views


app_name = 'groups'

urlpatterns = [
    url(r'^$', views.ListGroups.as_view(), name='all_groups' ),
    url(r'^new/$', views.CreateGroup.as_view(), name='create_group'),
    url(r'^post/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
]
