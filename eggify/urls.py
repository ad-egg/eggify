#!/usr/bin/python3
"""DOCSTRING FOR MODULE"""

from django.conf.urls import handler404
from django.urls import path

from . import views


app_name = 'eggify'
urlpatterns = [
    path('eggify/', views.index, name='index'),
    # ex: /egged/
    path('eggify/egged/', views.egged, name='egged'),
    # ex: /eggnt/95643f32-100b-4941-bff6-f4852e5c25cd/
    path('eggify/eggnt/<str:eggnt_uid>/', views.detail, name='detail'),
]

handler404 = 'eggify.views.error_404'
