#!/usr/bin/python3
"""MODULE FOR FORMS CLASSES"""

from django import forms


class InputForm(forms.Form):
    """a class InputForm"""
    your_input = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(initial='English', choices=[
            ('English', 'English'),
            ('Spanish', 'Español'),
            ('French', 'Français'),
            ('hanzi', '漢字'),
            ('Italian', 'Italiano'),
            ('Latin', 'Latin'),
            ('Portuguese', 'Português'),
    ])
