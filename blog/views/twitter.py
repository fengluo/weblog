#!/usr/bin/env python
# encoding: utf-8
"""
twitter.py

Created by Lawliet on 2011-02-01.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import time
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

from blog.models import UserMeta

from oauth.oauth import OAuthToken
from blog.twitter.oauthtwitter import OAuthApi

from weblog.config import twitter_consumer_key as CONSUMER_KEY
from weblog.config import twitter_consumer_secret as CONSUMER_SECRET


def home(request):
    """docstring for home"""
    if request.user.is_authenticated():
        user_meta=UserMeta.objects.filter(user=request.user)
        usermeta={}
        for u in user_meta:
            usermeta[u.key]=u.value
        
        twitter_access_token_string=UserMeta.objects.get(user=request.user,key="twitter_access_token_string").value
        access_token=OAuthToken.from_string(twitter_access_token_string)
        twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,access_token)
        statuses=twitter.GetHomeTimeline(count=20)
        i=0
        for status in statuses:
            # statuses[i].source=statuses[i].source.replace('<a', '<a class="dark"')
            statuses[i].datetime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y')))
            statuses[i].text = twitter.ConvertMentions(status.text)
            i=i+1
                
        return render_to_response('desktop/twitter.html',{'statuses':statuses,'usermeta':usermeta})
    else:
        return HttpResponseRedirect("/login")

def mentions(request):
    """docstring for mentions"""
    if request.user.is_authenticated():
        user_meta=UserMeta.objects.filter(user=request.user)
        usermeta={}
        for u in user_meta:
            usermeta[u.key]=u.value
        
        twitter_access_token_string=UserMeta.objects.get(user=request.user,key="twitter_access_token_string").value
        access_token=OAuthToken.from_string(twitter_access_token_string)
        twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,access_token)
        statuses=twitter.GetReplies()
        i=0
        for status in statuses:
            # statuses[i].source=statuses[i].source.replace('<a', '<a class="dark"')
            statuses[i].datetime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y')))
            statuses[i].text = twitter.ConvertMentions(status.text)
            i=i+1
        
        return render_to_response('desktop/twitter.html',{'statuses':statuses,'usermeta':usermeta})
    else:
        return HttpResponseRedirect("/login")

def messages(request):
    """docstring for messages"""
    if request.user.is_authenticated():
        user_meta=UserMeta.objects.filter(user=request.user)
        usermeta={}
        for u in user_meta:
            usermeta[u.key]=u.value
        
        twitter_access_token_string=UserMeta.objects.get(user=request.user,key="twitter_access_token_string").value
        access_token=OAuthToken.from_string(twitter_access_token_string)
        twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,access_token)
        statuses=twitter.GetDirectMessages()
        i=0
        for status in statuses:
            # statuses[i].source=statuses[i].source.replace('<a', '<a class="dark"')
            statuses[i].datetime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y')))
            statuses[i].text = twitter.ConvertMentions(status.text)
            i=i+1
        
        return render_to_response('desktop/twitter_messages.html',{'statuses':statuses,'usermeta':usermeta})
    else:
        return HttpResponseRedirect("/login")

def newtweet(request):
    if request.user.is_authenticated():
        user_meta=UserMeta.objects.filter(user=request.user)
        usermeta={}
        for u in user_meta:
            usermeta[u.key]=u.value
        
        status=self.request.get('status')
        if len(status) > 140:
            status=status[0:140]
        
        twitter_access_token_string=UserMeta.objects.get(user=request.user,key="twitter_access_token_string").value
        access_token=OAuthToken.from_string(twitter_access_token_string)
        twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,access_token)
        try:
            twitter.PostUpdate(status.encode('utf-8'))
        except:
            logging.error('Failed to tweet: '+status)
            
        return HttpResponseRedirect("/home")
    else:
        return HttpResponseRedirect("/login")