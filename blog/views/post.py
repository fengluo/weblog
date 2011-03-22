#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Lawliet on 2011-01-17.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

import time
import datetime

from blog.forms import PostForm
from blog.models import Post,Tag,UserMeta

def index(request):
    """docstring for index"""
    posts = Post.objects.all()
    return render_to_response('desktop/index.html',{'posts':posts})

def PostHandler(request,**args):
    """docstring for GetPost"""   
    if args["action"] =='get':
        post=Post.objects.get(id=args["id"])
        return render_to_response('desktop/post.html',{'post':post})
    
    if request.user.is_authenticated():
        if args["action"] =='del':
            p=Post.objects.get(id=args["id"])
            p.delete()
            return HttpResponseRedirect("/home")
        if args["action"] =='new':
            pageinfo={'title':"New Post",'action':'/p/add','button':'Publish'}
            return render_to_response('desktop/edit.html',{'pageinfo':pageinfo})
        if args["action"] =='add':
            if request.method == 'POST':
                form=PostForm(request.POST)
                if form.is_valid():
                    postform=form.cleaned_data
                    user=request.user
                    published=datetime.datetime.now()
                    post=Post(title=postform['title'],url=postform['url'],author=user,content=postform['content'],published=published)
                    post.save()
                    
                    tags=postform['tags'].split(" ")
                    if tags:
                        for t in tags:
                            try:
                                tag=Tag.objects.get(name=t)
                            except Tag.DoesNotExist:
                                tag=Tag(name=t)
                                tag.save()
                            post.tags.add(tag)
                    
                                       
            return HttpResponseRedirect('/home')
        
        if args["action"]=='edit':
            pageinfo={'title':"Edit Post",'action':'/p/update/'+args["id"],'button':'Update'}
            postform=Post.objects.get(id=args["id"])
            # tags=[ t.tag.name  for t in Post2Tag.objects.filter(post=args["id"])]
            #             tags=' '.join(tags)
            tags=postform.tags.all()
            return render_to_response('desktop/edit.html',{'pageinfo':pageinfo,'postform':postform,'tags':tags})
        
        if args["action"]=='update':
            if request.method=='POST':
                form=PostForm(request.POST)
                if form.is_valid():
                    postform=form.cleaned_data
                    user=request.user
                    post=Post.objects.get(id=args["id"])
                    post.title=postform['title']
                    post.url=postform['url']
                    post.content=postform['content']
                    post.save()
                    
                    newtags=[tag.strip() for tag in postform['tags'].split()]
                    oldtags=[tag.name for tag in post.tags.all()]
                    
                    for t in list(set(oldtags).difference(set(newtags))):
                        post.tags.remove(Tag.objects.get(name=t))
                    
                    for t in list(set(newtags).difference(set(oldtags))):
                        try:
                            tag=Tag.objects.get(name=t)
                        except Tag.DoesNotExist:
                            tag=Tag(name=t)
                            tag.save()
                        post.tags.add(Tag.objects.get(name=t))
                    
            return HttpResponseRedirect('/home')        
    else:
        return HttpResponseRedirect("/login")    



def home(request):
    """docstring for home"""
    if request.user.is_authenticated():
        posts = Post.objects.all()
        user=request.user
        
        # twitter_access_token_string=UserMeta.objects.get(user=user,key="twitter_access_token_string").value
        #         access_token=OAuthToken.from_string(twitter_access_token_string)
        #         twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,access_token)
        #         statuses=twitter.GetHomeTimeline(count=20)
        #         i=0;
        #         for status in statuses:
        #             # statuses[i].source=statuses[i].source.replace('<a', '<a class="dark"')
        #             statuses[i].datetime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(status.created_at, '%a %b %d %H:%M:%S +0000 %Y')))
        #             statuses[i].text = twitter.ConvertMentions(status.text)
        #             i=i+1
        #         
        return render_to_response('desktop/home.html',{'posts':posts,'user':user})
    else:
        return HttpResponseRedirect("/login")


