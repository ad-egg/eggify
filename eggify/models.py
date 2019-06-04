#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import uuid

from django.db import models

class Eggnt(models.Model):
    """a class Eggnt"""

    def __str__(self):
        """returns the words"""
        return self.words

    uid = models.CharField(max_length=50, default=str(uuid.uuid4()), editable=False)
    words = models.CharField(max_length=5000, editable=False)
    created_at = models.DateTimeField('created at', editable=False)
#    user_num = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

class User(models.Model):
    """a class User"""
#    num = models.IntegerField()
#    name = models.CharField(max_length=50)
    pass
