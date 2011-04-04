from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import Sum


class SnippetManager(models.Manager):
    """Custom manager for Snippet Model
    """
    def top_authors(self):
        return User.objects.annotate(score=Count('snippet')).order_by('score')

    def most_bookmarked(self):
            return self.annotate(score=Count('bookmark')).order_by('-score')

    def top_rated(self):
            return self.annotate(score=Sum('rating')).order_by('score')

class LanguageManager(models.Manager):
    """Custom Manager for Language Model
    """
    def top_languages(self):
        return self.annotate(score=Count('snippet')).order_by('score')


