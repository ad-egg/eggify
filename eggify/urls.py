#!/usr/bin/python3
"""DOCSTRING FOR MODULE"""

from django.conf.urls import handler404
from django.urls import path

from . import views


app_name = 'eggify'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /egged/
    path('egged/', views.egged, name='egged'),
    # ex: /eggnt/95643f32-100b-4941-bff6-f4852e5c25cd/
    path('eggnt/<str:eggnt_uid>/', views.detail, name='detail'),
    # ex: /eggnt/
    path('eggnt/', views.eggnt, name='eggnt'),
]

handler404 = 'eggify.views.error_404'
