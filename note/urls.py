from django.conf.urls import patterns, url
from note import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.register, name='register'),
        url(r'^upload/$', views.create, name='create'), #'list' might need to be views.list
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'subject/(?P<subject_name_slug>[\w\-]+)/$', views.subject, name='subject'),
        url(r'subject/(?P<subject_name_slug>[\w\-]+)/(?P<module_abb>[\w\-]+)/$', views.module, name='module'),
        url(r'^profile/', views.profile, name='profile'),                                             #Don't delete, I am trying to get this working
		)