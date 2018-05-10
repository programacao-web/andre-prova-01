from django.shortcuts import render, redirect, get_object_or_404
from pastebin.forms import PasteForm
from pastebin.models import Paste
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

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

    lexer = get_lexer_by_name(paste.language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="code-highlight")
    result = highlight(paste.code_body, lexer, formatter)

    ctx = {
        'result': result,
        'paste': paste
    }
    return render(request, 'pastebin/paste-detail.jinja2', ctx)

def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)
