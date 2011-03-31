from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from app.models import Snippet
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author']
    
@csrf_exempt 
def add_snippet(request):
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

@csrf_exempt 
def edit_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if request.user.id != snippet.author.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        form = SnippetForm(instance=snippet)
    return render_to_response('app/snippet_form.html',
                                { 'form': form, 'add': False },
                                context_instance=RequestContext(request))
edit_snippet = login_required(edit_snippet)

