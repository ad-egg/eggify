#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import re
import uuid

from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import TemplateView

from .forms import InputForm
from .models import Eggnt


def index(request):
    form = InputForm()
    return render(request, 'eggify/index.html', {
            'form': form,
            'cache_id': str(uuid.uuid4()),
            })

def egged(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            words = form.cleaned_data['your_input']
            output_language = form.cleaned_data['output_language']
            input_language = form.cleaned_data['input_language']
            eggnt = Eggnt.create(words)
            eggnt.save()
            egg = to_egg(eggnt.words, output_language)
            host_name = request.get_host()
            return render(request, 'eggify/egged.html', {
                    'egg': egg,
                    'eggnt': eggnt,
                    'host_name': host_name,
                    'cache_id': str(uuid.uuid4()),
                    })
    elif request.method == 'GET':
        return redirect('eggify:index')

def detail(request, eggnt_uid):
    try:
        eggnt = Eggnt.objects.get(pk=eggnt_uid)
    except Eggnt.DoesNotExist:
        raise Http404("Unfortuneggly, there is no entry by that ID.")
    return render(request, 'eggify/detail.html', {
            'eggnt': eggnt,
            'cache_id': str(uuid.uuid4()),
            })

def eggnt(request):
    raise Http404("Nothing to see here.")

def error_404(request, exception):
    data = {
        'exception': exception,
        'cache_id': str(uuid.uuid4()),
    }
    return render(request, '404.html', data)

def to_egg(words, output_language):
    """turns all the words into egg and every digit into 0"""
    egg_languages = {
        'English': 'egg',
        'French': 'oeuf',
        'Spanish': 'huevo',
        'Latin': 'ovum',
        'Portuguese': 'ovo',
        'Italian': 'uovo',
        'hanzi': '蛋'
    }
    egged = re.sub(r'[a-z|A-Z]+', egg_languages[output_language], words)
    egged = re.sub(r'[1-9]', '0', egged)
    if output_language == 'hanzi':
        egged = egged.replace('蛋 蛋', '蛋蛋')
        egged = egged.replace('蛋 蛋', '蛋蛋')
    return egged
