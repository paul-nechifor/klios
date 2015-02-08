from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^check$', views.check, name='check'),
    url(r'^rate$', views.rate, name='rate'),
    url(r'^finish$', views.finish, name='finish'),
    url(r'^all$', views.all, name='all'),
)
