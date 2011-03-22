#!/usr/bin/env python
# encoding: utf-8
"""
setting.py

Created by Lawliet on 2011-02-01.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

from blog.forms import SiteMetaForm
from blog.models import SiteMeta,UserMeta

def setting(request):
    """docstring for setting"""           
    if request.user.is_authenticated():
        if request.method=='POST':
            form=SiteMetaForm(request.POST)
            if form.is_valid():
                sitemetaform=form.cleaned_data
                try:
                    sitemeta=SiteMeta.objects.get(key='sitetitle')
                    sitemeta.value=sitemetaform['sitetitle']
                    sitemeta.save()
                except SiteMeta.DoesNotExist:
                    sitemeta=SiteMeta(key='sitetitle',value=sitemetaform['sitetitle'])
                    sitemeta.save()
                
                try:
                    sitemeta=SiteMeta.objects.get(key='tagline')
                    sitemeta.value=sitemetaform['tagline']
                    sitemeta.save()
                except SiteMeta.DoesNotExist:
                    sitemeta=SiteMeta(key='tagline',value=sitemetaform['tagline'])
                    sitemeta.save()
                    
                try:
                    sitemeta=SiteMeta.objects.get(key='bio')
                    sitemeta.value=sitemetaform['bio']
                    sitemeta.save()
                except SiteMeta.DoesNotExist:
                    sitemeta=SiteMeta(key='bio',value=sitemetaform['bio'])
                    sitemeta.save()
                    
                return HttpResponseRedirect("setting")
        else:
            site=SiteMeta.objects.all()
            sitemeta={}
            for s in site:
                sitemeta[s.key]=s.value
            user_meta=UserMeta.objects.filter(user=request.user)
            usermeta={}
            for u in user_meta:
                usermeta[u.key]=u.value
            return render_to_response('desktop/setting.html',{'sitemeta':sitemeta,'usermeta':usermeta})
    else:
        return HttpResponseRedirect("/login")