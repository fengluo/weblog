from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
# from django.http import HttpRequest

from oauthtwitter import OAuthApi
import twitter as t

from blog.models import UserMeta

from weblog.config import twitter_consumer_key as CONSUMER_KEY
from weblog.config import twitter_consumer_secret as CONSUMER_SECRET

def Auth(request):
    """docstring for Auth"""
    twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET)
    request_token=twitter.getRequestToken()
    authorization_url=twitter.getAuthorizationURL(request_token)
    request.session['request_token']=request_token
    return HttpResponseRedirect(authorization_url)

def Callback(request):
    """docstring for Callback"""
    verifier=request.GET.get('oauth_verifier',None)
    request_token=request.session['request_token']
    twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,request_token)
    # twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET)
    # access_token=twitter.getAccessToken(request_token,verifier)
    access_token=twitter.getAccessToken()
    # api=t.Api(CONSUMER_KEY,CONSUMER_SECRET,access_token['oauth_token'],access_token['oauth_token_secret'])
    twitter=OAuthApi(CONSUMER_KEY,CONSUMER_SECRET,access_token)
    # user=api.GetUserInfo()
    user=twitter.GetUserInfo()
    twitter_auth=UserMeta(user=request.user,key="oauth",value=1)
    twitter_auth.save()
    # twitter_access_token_key=UserMeta(user=request.user,key="access_token_key",value=access_token['oauth_token'])
    # twitter_access_token_key.save()
    # twitter_access_token_secret=UserMeta(user=request.user,key="access_token_secret",value=access_token['oauth_token_secret'])
    # twitter_access_token_secret.save()
    twitter_access_token_string=UserMeta(user=request.user,key="twitter_access_token_string",value=access_token.to_string())
    twitter_access_token_string.save()
    twitter_id=UserMeta(user=request.user,key="twitter_id",value=user.id)
    twitter_id.save()
    twitter_name=UserMeta(user=request.user,key="twitter_name",value=user.name)
    twitter_name.save()
    twitter_screen_name=UserMeta(user=request.user,key="twitter_screen_name",value=user.screen_name)
    twitter_screen_name.save()
    twitter_description=UserMeta(user=request.user,key="twitter_description",value=user.description)
    twitter_description.save()
    twitter_profile_image_url=UserMeta(user=request.user,key="twitter_profile_image_url",value=user.profile_image_url)
    twitter_profile_image_url.save()
    return HttpResponseRedirect("/setting")