from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
import settings # probably not required
from django.conf import settings
from django.conf.urls.static import static
from note import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^note/', include('note.urls')),
   # (r'^', include('note.urls')),
    url(r'^note/', include('note.urls'), # dont know if this is corrrect
        ))\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # ) ) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) # this only works in production...



if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )