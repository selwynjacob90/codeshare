from django.db import models

from pygments import lexers

class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    language_code = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ('cab_language_detail', (), { 'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)

