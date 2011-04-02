from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^main_site/', include('main_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/slingshot316/my-python-code/django-projects/codeshare/app/content'}),

    #codeshare url's
    (r'^snippets/', include('app.urls.snippets')),
    (r'^languages/', include('app.urls.languages')),
    (r'^popular/', include('app.urls.popular')),
    (r'^$', include('app.urls.home')),
)
