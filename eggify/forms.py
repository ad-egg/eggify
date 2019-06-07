#!/usr/bin/python3
"""MODULE FOR FORMS CLASSES"""

from django import forms


class InputForm(forms.Form):
    """a class InputForm"""
    your_input = forms.CharField(widget=forms.Textarea)
