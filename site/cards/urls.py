from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^check$', views.check, name='check'),
    url(r'^rate$', views.rate, name='rate'),
    url(r'^finish$', views.finish, name='finish'),
)
