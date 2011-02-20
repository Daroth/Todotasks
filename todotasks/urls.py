from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Example:
                       # (r'^todotasks/', include('todotasks.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^admin/', include(admin.site.urls)),

                       (r'^', include('apps.tasks.urls')),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='log-in'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           {'next_page':'/', 'redirect_field_name':'next',}, name='log-out'),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                                })
                            )