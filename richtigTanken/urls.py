from django.conf.urls import patterns, url

from richtigTanken import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'newValue/', views.addWaypoint, name='location_update'),
    url(r'endRoute/', views.endRoute, name='stopRoute'),
)