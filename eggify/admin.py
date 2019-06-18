#!/usr/bin/python3
"""DOCSTRING GOES HERE"""
from django.contrib import admin

from .models import Eggnt


class EggntAdmin(admin.ModelAdmin):
    fieldsets = [
# the following fieldsets are commented out because editable=False
#        ('ID', {'fields': ['id']}),
#        ('Date and time information', {'fields': ['created_at']}),
        ('User input', {'fields': ['words']}),
        ('Language', {'fields': ['language']}),
    ]
    list_display = ('created_at', 'id', 'language',  'words')
    list_filter = ['created_at']
    ordering = ('-created_at',)
    search_fields = ['words']

admin.site.register(Eggnt, EggntAdmin)
