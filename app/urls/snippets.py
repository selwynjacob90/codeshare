from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from app.models import Snippet
from app.views.snippets import add_snippet, edit_snippet

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

                       url(r'^add/$',
                           add_snippet,
                           name='app_snippet_add'),

                       url(r'^edit/(?P<snippet_id>\d+)/$',
                           edit_snippet,
                           name='app_snippet_edit'),
                     )
