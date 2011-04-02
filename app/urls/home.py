from django.conf.urls.defaults import *
from app.views.home import home

urlpatterns = patterns('',
    url(r'^$', home, name='app_home'),
)

