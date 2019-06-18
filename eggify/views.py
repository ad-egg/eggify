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
    location = 'Holberton<br>972 Mission St.<br>San Francisco, CA 94103'
    form = InputForm()
    return render(request, 'eggify/index.html', {'theme': theme, 'form': form, 'cache_id': str(uuid.uuid4()), 'location': location})

def egged(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            theme = "yellow_egg"
            location = 'Holberton<br>972 Mission St.<br>San Francisco, CA 94103'
            words = form.cleaned_data['your_input']
            output_language = form.cleaned_data['output_language']
            eggnt = Eggnt.create(words)
            eggnt.save()
            egg = to_egg(eggnt.words, output_language)
            host_name = request.get_host()
            return render(request, 'eggify/egged.html', {'theme': theme, 'egg': egg, 'eggnt': eggnt, 'host_name': host_name, 'cache_id': str(uuid.uuid4()), 'location': location})

def detail(request, eggnt_uid):
    try:
        eggnt = Eggnt.objects.get(pk=eggnt_uid)
    except Eggnt.DoesNotExist:
        raise Http404("Unfortuneggly, there is no entry by that ID.")
    theme = "yellow_egg"
    location = 'Holberton<br>972 Mission St.<br>San Francisco, CA 94103'
    return render(request, 'eggify/detail.html', {'theme': theme, 'eggnt': eggnt, 'cache_id': str(uuid.uuid4()), 'location': location})

def error_404(request, exception):
    theme = "yellow_egg"
    location = 'Holberton<br>972 Mission St.<br>San Francisco, CA 94103'
    data = {'exception': exception, 'theme': theme, 'cache_id': str(uuid.uuid4()), 'location': location}
    return render(request, '404.html', data)

def to_egg(words, output_language):
    """turns all the words into egg and every digit into 0"""
    egg_languages = {'English': 'egg', 'French': 'oeuf', 'Spanish': 'huevo', 'Latin': 'ovum', 'Portuguese': 'ovo', 'Italian': 'uovo', 'hanzi': '蛋'}
    egged = re.sub(r'[a-z|A-Z]+', egg_languages[language], words)
    egged = re.sub(r'[1-9]', '0', egged)
    return egged
