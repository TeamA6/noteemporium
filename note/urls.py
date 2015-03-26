from django.conf.urls import patterns, url
from note import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.register, name='register'),
        url(r'^upload/$', views.create, name='create'), #'list' might need to be views.list
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'subject/(?P<subject_name_slug>[\w\-]+)/$', views.subject, name='subject'),
        url(r'subject/(?P<subject_name_slug>[\w\-]+)/(?P<module_abb>[\w\-]+)/$', views.view_notes, name='view_notes'),
        url(r'subject/(?P<subject_name_slug>[\w\-]+)/(?P<module_abb>[\w\-]+)/create/$',views.create, name='create'),
        url(r'^profile/', views.profile, name='profile'),
        url(r'^latest/', views.latest, name='latest'),
        url(r'^search/', views.search, name='search'),
        url(r'^reported/(?P<slugTitle>[\w\-]+)/$', views.reported, name='reported'),
		)
