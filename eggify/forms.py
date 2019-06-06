#!/usr/bin/python3
"""MODULE FOR FORMS CLASSES"""

from django import forms


class InputForm(forms.Form):
    """a class InputForm"""
    input = forms.CharField(widget=forms.Textarea)

class OutputForm(forms.Form):
    """a class OutputForm"""
    output = forms.CharField(widget=forms.Textarea)

class LinkForm(forms.Form):
    """a class LinkForm"""
    link = forms.CharField()
