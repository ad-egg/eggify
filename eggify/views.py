#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import re

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView

from .forms import InputForm, LinkForm, OutputForm
from .models import Eggnt


def index(request):
    form = InputForm()
    return render(request, 'eggify/index.html', {'form': form})

def egged(request):
    egged = OutputForm()
    link = LinkForm()
    return render(request, 'eggify/egged.html', {'box': egged, 'link': link})

def detail(request, eggnt_uid):
    try:
        eggnt = Eggnt.objects.get(pk=eggnt_uid)
    except Eggnt.DoesNotExist:
        raise Http404("There is no entry by that ID.")
    return render(request, 'eggify/detail.html', {'eggnt': eggnt})

def post_words(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['input']
            eggnt = Eggnt(words=user_input)
            eggnt.save()
# pass the eggnt.id to get_link
#        DO THINGS
#            pass
#        pass
# this method is supposed to save the client input into the database, get the ID of the input, call to_egg to turn the input into egg, somewhere there should be a function or something that puts together the URL for the client input
        

# def to_egg(words, egg="egg"):
#    """turns all the words into egg"""
#    egged = re.sub(r'[a-z|A-Z]+', egg, words)
#    return egged

# def get_eggs(request):
# this method is supposed to get the eggified string and display it in the output form

# def get_link(request):
# this method is to get the ID of the client input from the database and return a URL
