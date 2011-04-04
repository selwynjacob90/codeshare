from django.conf.urls.defaults import *
from app.views.ratings import rate

urlpatterns = patterns('',
    url(r'^(?P<snippet_id>\d+)$', rate, name='app_snippet_rate'),
)
