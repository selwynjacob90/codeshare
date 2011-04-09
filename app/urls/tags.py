from django.conf.urls.defaults import *
from app.models import Snippet
from tagging.models import Tag
import tagging 

urlpatterns = patterns('',
    (r'^(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list', { 
        'queryset_or_model': Snippet.objects.all(), 
        'template_name': 'app/snippets_by_tag.html'
    }, 'app_snippet_archive_tag'),
)
