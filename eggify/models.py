#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import uuid

# from datetime import datetime
from django.db import models
from django.utils import timezone


class Eggnt(models.Model):
    """a class Eggnt"""

    # fields/columns in database
    id = models.CharField(max_length=50, default=str(uuid.uuid4()), primary_key=True, editable=False)
    updated_at = models.DateTimeField('updated at', default=timezone.now(), editable=False)
    words = models.TextField(null=False, editable=False, help_text='Enter text to be eggified!')
#    user_num = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    # metadata
    class Meta:
        ordering = ['-updated_at']

    # methods
    def __str__(self):
        """returns the words"""
        return self.words

    @classmethod
    def create(cls, words):
        """creates a new Eggnt object"""
        eggnt = cls(words=words, id=str(uuid.uuid4()))
        return eggnt

    @classmethod
    def update(cls, words):
        """creates a new Eggnt object every time"""
        eggnt = cls(words=words, id=str(uuid.uuid4()))
        return eggnt


class User(models.Model):
    """a class User"""
#    num = models.IntegerField()
#    name = models.CharField(max_length=50)
    pass
