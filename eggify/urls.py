#!/usr/bin/python3
"""DOCSTRING FOR MODULE"""

from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name='index'),
]
