#!/usr/bin/python3
"""DOCSTRING GOES HERE"""
from django.contrib import admin

from .models import Eggnt


class EggntAdmin(admin.ModelAdmin):
    fieldsets = [
#        ('ID', {'fields': ['id']}),
#        ('Date and time information', {'fields': ['updated_at']}),
        ('User input', {'fields': ['words']}),
    ]
    list_display = ('updated_at', 'id', 'words')
    list_filter = ['updated_at']
    search_fields = ['words']

admin.site.register(Eggnt, EggntAdmin)
