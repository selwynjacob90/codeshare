from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from app.models import Snippet

snippet_info = { 'queryset' : Snippet.objects.all() }

urlpatterns = patterns('',
                       url(r'^$',
                           object_list,
                           dict(snippet_info, paginate_by = 20),
                           name = 'app_snippet_list'),
                       
                       url(r'^(?P<object_id>\d+)/$',
                           object_detail,
                           snippet_info,
                           name = 'app_snippet_detail'),
                     )
