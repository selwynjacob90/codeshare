from django.conf.urls.defaults import *
from app.views import popular

urlpatterns = patterns('',
                       url(r'^authors/$',
                           popular.top_authors,
                           name = 'app_top_authors'),
                       url(r'^languages/$',
                           popular.top_languages,
                           name='app_top_languages'),
                       url(r'^bookmarks/$',
                           popular.most_bookmarked, 
                           name='app_most_bookmarked'),
                       url(r'^ratings/$', 
                           popular.top_rated, 
                           name='app_top_rated'),
                      )
