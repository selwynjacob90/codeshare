from django.contrib.auth.models import User
from django.views.generic.list_detail import object_list

from django.db.models import Count

def top_authors(request):
    return object_list(request, queryset=Snippet.objects.top_authors(),
                       template_name='app/top_authors.html',
                       paginate_by=20)


