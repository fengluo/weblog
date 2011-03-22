#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

from datetime import datetime

class Tag(models.Model):
    name=models.CharField(max_length=20)

class Post(models.Model):
    # title=models.CharField(max_length=140)
    title=models.TextField(validators=[MaxLengthValidator(140)])
    url=models.CharField(max_length=50)
    author=models.ForeignKey(User)
    content=models.TextField()
    tags=models.ManyToManyField(Tag)
    created=models.DateTimeField(default=datetime.now, editable=False)
    published=models.DateTimeField(editable=False)
    views=models.IntegerField(default=0,editable=False)

class SiteMeta(models.Model):
    """docstring for SiteMeta"""
    key=models.CharField(max_length=140)
    value=models.CharField(max_length=140)

class UserMeta(models.Model):
    """docstring for UserMeta"""
    user=models.ForeignKey(User)
    key=models.CharField(max_length=255)
    # value=models.CharField(max_length=255)
    value=models.TextField()