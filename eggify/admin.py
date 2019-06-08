#!/usr/bin/python3
"""DOCSTRING GOES HERE"""
from django.contrib import admin

from .models import Eggnt


class EggntAdmin(admin.ModelAdmin):
    fieldsets = [
# the following two fieldsets are commented out because editable=False
#        ('ID', {'fields': ['id']}),
#        ('Date and time information', {'fields': ['updated_at']}),
        ('User input', {'fields': ['words']}),
    ]
    list_display = ('updated_at', 'id', 'words')
    list_filter = ['updated_at']
    ordering = ('-updated_at',)
    search_fields = ['words']

admin.site.register(Eggnt, EggntAdmin)
