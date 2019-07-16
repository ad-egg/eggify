#!/usr/bin/python3
"""this module contains the class definition for InputForm"""

from django import forms


class InputForm(forms.Form):
    """
    a class used to represent an input form
    
    ...
    
    Attributes
    ----------
    input_language : str
        a string that specifies the input language of a user's entry (default 'English')
    your_input: str
        a user's input
    output_language : str
        the output language the user wants
        
    Methods
    -------
    
    
    """
    input_language = forms.ChoiceField(initial='English', choices=[
            ('English', 'English')
    ])
    your_input = forms.CharField(widget=forms.Textarea)
    output_language = forms.ChoiceField(initial='English', choices=[
            ('English', 'English'),
            ('Spanish', 'Español'),
            ('French', 'Français'),
            ('hanzi', '漢字'),
            ('Italian', 'Italiano'),
            ('Latin', 'Latin'),
            ('Portuguese', 'Português'),
    ])
