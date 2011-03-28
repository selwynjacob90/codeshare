from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from app.models import Snippet


class SnippetForm(ModelForm):
"""Automatically generate form from Snippet Model.
"""
    class Meta:
        model = Snippet
        exclude = ['author']
    
def add_snippet(request):
"""view to add a snippet.
"""
    if request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet.author = request.user
            new_snippet.save()
            return HttpResponseRedirect(new_snippet.get_absolute_url())
    else:
        form = SnippetForm()
    return render_to_response('app/snippet_form.html', 
                              { 'form': form, 'add': True },
                              context_instance=RequestContext(request))

add_snippet = login_required(add_snippet)


