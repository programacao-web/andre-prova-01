from django.shortcuts import render, redirect, get_object_or_404
from pastebin.forms import PasteForm
from pastebin.models import Paste

def index(request):
    form = PasteForm()
    ctx = {}

    if request.method == 'GET':
        ctx["form"] = form
        return render(request, 'pastebin/index.jinja2', ctx)
    elif request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            a = form.save()
            return redirect('pastebin-detail', id=a.id)
        else:
            return render(request, 'pastebin/index.jinja2', { 'form': form })

def paste(request, id):
    paste = get_object_or_404(Paste, pk=id)
    ctx = {
        'paste': paste
    }
    return render(request, 'pastebin/paste-detail.jinja2', ctx)

def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)
