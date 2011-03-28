from django.conf.urls.defaults import *
from app.views import popular

urlpatterns = patterns('',
                       url(r'^authors/$',
                           popular.top_authors,
                           name = 'app_top_authors'),
                       url(r'^languages/$',
                           popular.top_languages,
                           name='app_top_languages'),
                      )
