#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Lawliet on 2011-01-18.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

from models import Post
from django import forms


class PostForm(forms.Form):
    """docstring for PostForm"""
    title = forms.CharField(widget=forms.Textarea,max_length = 140,required=True)
    url=forms.CharField(max_length=50,required=False)
    content=forms.CharField(widget=forms.Textarea,required=False)
    tags=forms.CharField(max_length=140,required=False)

class SiteMetaForm(forms.Form):
    """docstring for SiteMetaForm"""
    sitetitle=forms.CharField(max_length=140,required=False)
    tagline=forms.CharField(max_length=140,required=False)
    bio=forms.CharField(max_length=140,required=False)