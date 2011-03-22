from django.conf.urls.defaults import *
from app.views import popular

urlpatterns = patterns('',
                       url(r'^authors/$',
                           popular.top_authors,
                           name = 'app_top_authors'),
                      )
