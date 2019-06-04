#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the eggify index.")
