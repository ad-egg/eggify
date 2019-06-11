#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import re
import uuid

from django.http import Http404, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView

from .forms import InputForm
from .models import Eggnt


def index(request):
    theme = "yellow_egg"
    form = InputForm()
    return render(request, 'eggify/index.html', {'theme': theme, 'form': form, 'cache_id': str(uuid.uuid4())})

def egged(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            theme = "yellow_egg"
            words = form.cleaned_data['your_input']
            eggnt = Eggnt.create(words)
            eggnt.save()
            egg = to_egg(eggnt.words)
            host_name = request.get_host()
            return render(request, 'eggify/egged.html', {'theme': theme, 'egg': egg, 'eggnt': eggnt, 'host_name': host_name, 'cache_id': str(uuid.uuid4())})

def detail(request, eggnt_uid):
    try:
        eggnt = Eggnt.objects.get(pk=eggnt_uid)
    except Eggnt.DoesNotExist:
        raise Http404("Unfortuneggly, there is no entry by that ID.")
    theme = "yellow_egg"
    return render(request, 'eggify/detail.html', {'theme': theme, 'eggnt': eggnt, 'cache_id': str(uuid.uuid4())})

def error_404(request, exception):
    data = {'exception': exception}
    return render(request, '404.html', data)

def to_egg(words, egg="egg"):
    """turns all the words into egg and every digit into 0"""
    egged = re.sub(r'[a-z|A-Z]+', egg, words)
    egged = re.sub(r'[1-9]', '0', egged)
    return egged
