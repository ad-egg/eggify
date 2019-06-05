#!/usr/bin/python3
"""DOCSTRING FOR MODULE"""

from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name='index'),
    # ex: /eggnt/95643f32-100b-4941-bff6-f4852e5c25cd/
    path('eggnt/<str:eggnt_uid>/', views.detail, name='detail')
]
