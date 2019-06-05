#!/usr/bin/python3
"""MODULE FOR FORMS CLASSES"""

from django import forms


class EggntForm(forms.Form):
    """a class EggntForm"""
    eggnt = forms.CharField(widget=forms.Textarea)
