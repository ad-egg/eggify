#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import Eggnt


def index(request):
    return render(request, 'eggify/index.html', {})

def detail(request, eggnt_uid):
    try:
        eggnt = Eggnt.objects.get(pk=eggnt_uid)
    except Eggnt.DoesNotExist:
#        return render(request, 'eggify/404.html', {'eggnt': "There is no entry by that ID."})
        raise Http404("There is no entry by that ID.")
    return render(request, 'eggify/detail.html', {'eggnt': eggnt})
