#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import re

from django.http import Http404 # , HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView

from .forms import InputForm
from .models import Eggnt


def index(request):
    form = InputForm()
    return render(request, 'eggify/index.html', {'form': form})

def egged(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            words = form.cleaned_data['your_input']
            eggnt = Eggnt.create(words)
            eggnt.save()
            egg = to_egg(eggnt.words)
#            egg_html = whitespace_to_html(egg)
            return render(request, 'eggify/egged.html', {'egg': egg, 'eggnt': eggnt})

def detail(request, eggnt_uid):
    try:
        eggnt = Eggnt.objects.get(pk=eggnt_uid)
#        eggnt_html = whitespace_to_html(eggnt.words)
    except Eggnt.DoesNotExist:
        raise Http404("There is no entry by that ID.")
    return render(request, 'eggify/detail.html', {'eggnt': eggnt})

def to_egg(words, egg="egg"):
    """turns all the words into egg"""
    egged = re.sub(r'[a-z|A-Z]+', egg, words)
    return egged

def whitespace_to_html(words_w_whitespace):
    """replaces newline and tab character characters  with HTML tag for line break"""
    words_w_4space = words_w_whitespace.replace('    ', '&emsp;&emsp;')
    words_w_tab = words_w_4space.replace('\t', '&emsp;&emsp;&emsp;&emsp;')
    words_w_html = words_w_tab.replace('\n', '<br>')
    return words_w_html
