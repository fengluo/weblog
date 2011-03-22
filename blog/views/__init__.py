#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Lawliet on 2011-02-01.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

def login(request):
    """docstring for login"""
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect("/home")
    else:
        return render_to_response('desktop/login.html')

def logout(request):
    """docstring for logout"""
    auth.logout(request)
    return HttpResponseRedirect("/")