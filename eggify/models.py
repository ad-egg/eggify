#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import uuid

from django.db import models
from django.utils import timezone


class Eggnt(models.Model):
    """a class Eggnt"""

    # fields/columns in database
    id = models.CharField(max_length=255, default=str(uuid.uuid4()), primary_key=True, editable=False)
    created_at = models.DateTimeField('created at', default=timezone.now(), editable=False)
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
