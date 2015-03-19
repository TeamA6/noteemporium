from django.conf.urls import patterns, url
from note import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.register, name='register'),
        url(r'^upload/$', views.list, name='list'), #'list' might need to be views.list
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
		)