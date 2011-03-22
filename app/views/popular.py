from django.contrib.auth.models import User
from django.views.generic.list_detail import object_list

from django.db.models import Count

def top_authors(request):
    top_authors_qs = User.objects.annotate(score=Count('snippet')).order_by('score')
    return object_list(request, queryset=top_authors_qs,
                       template_name='app/top_authors.html',
                       paginate_by=20)


