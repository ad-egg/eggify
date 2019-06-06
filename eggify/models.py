#!/usr/bin/python3
"""DOCSTRING GOES HERE"""

import uuid

# from datetime import datetime
from django.db import models
from django.utils import timezone


class Eggnt(models.Model):
    """a class Eggnt"""

    def __str__(self):
        """returns the words"""
        return self.words

    id = models.CharField(max_length=50, default=str(uuid.uuid4()), primary_key=True)
    updated_at = models.DateTimeField('updated at', default=timezone.now())
    words = models.CharField(max_length=5000)
#    user_num = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

class User(models.Model):
    """a class User"""
#    num = models.IntegerField()
#    name = models.CharField(max_length=50)
    pass
