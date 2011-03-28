from django.contrib.auth.models import User
from django.views.generic.list_detail import object_list

from django.db.models import Count

from app.models import Language, Snippet


def top_authors(request):
    """ view to return the top authors
    """
    return object_list(request, queryset=Snippet.objects.top_authors(),
                       template_name='app/top_authors.html',
                       paginate_by=20)

def top_languages(request):
    """ view to return the top languages
    """
    return object_list(request, queryset=Language.objects.top_languages(),
                       template_name='app/top_languages.html',
                       paginate_by=20)


