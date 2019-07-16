#!/usr/bin/python3
"""this module contains class definition for Eggnt"""

import uuid

from django.db import models
from django.utils import timezone


class Eggnt(models.Model):
    """
    a class used to represent a user's input

    ...

    Attributes
    ----------
    id : str
        a unique string that identifies a Eggnt object
    created_at : datetime
        records when an object was created
    input_language : str
        a string that represents the language of the user's input (default "English")
    words : str
        the user's input

    Methods
    -------
    __str__(self):
        prints the user's input string that is associated with the object
    create(cls, words):
        creates a new Eggnt object
    update(cls, words):
        overrides default update method to ensure a new object is created every time
    """

    # languages
    ENGLISH = 'EN'
    LANGUAGE = [
        (ENGLISH, 'English')
    ]

    # fields/columns in database
    id = models.CharField(max_length=255, default=str(uuid.uuid4()), primary_key=True, editable=False)
    created_at = models.DateTimeField('created at', default=timezone.now(), editable=False)
    input_language = models.CharField(max_length=2, choices=LANGUAGE, default=ENGLISH)
    words = models.TextField(null=False, help_text='Enter text to be eggified!')
#    user_num = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    # metadata
    class Meta:
        ordering = ['-created_at']

    # methods
    def __str__(self):
        """returns the words"""
        return self.words

    @classmethod
    def create(cls, words):
        """creates a new Eggnt object"""
        eggnt = cls(words=words, id=str(uuid.uuid4()), created_at=timezone.now())
        return eggnt

    @classmethod
    def update(cls, words):
        """creates a new Eggnt object every time"""
        return cls.create(words)


class User(models.Model):
    """a class User"""
#    num = models.IntegerField()
#    name = models.CharField(max_length=50)
    pass
