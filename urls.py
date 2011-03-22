from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf import settings

from blog.views import *
from blog.views import post,twitter,setting
from blog.twitter import Auth,Callback

urlpatterns = patterns('',
    # Example:
    # (r'^weblog/', include('weblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
    (r'^$', post.index),
    (r'^p/(?P<id>\d+)$',post.PostHandler,{'action':'get'}),
    (r'^p/new$',post.PostHandler,{'action':'new'}),
    (r'^p/add$',post.PostHandler,{'action':'add'}),
    (r'^p/del/(?P<id>\d+)$',post.PostHandler,{'action':'del'}),
    (r'^p/edit/(?P<id>\d+)$',post.PostHandler,{'action':'edit'}),
    (r'^p/update/(?P<id>\d+)$',post.PostHandler,{'action':'update'}),
    (r'^login$',login),
    (r'^logout$',logout),
    (r'^home$',post.home),
    (r'^setting$',setting.setting),
    (r'^updatesitemeta$',setting.setting),
    (r'^twitter/auth$',Auth),
    (r'^twitter/callback$',Callback),
    (r'^twitter$',twitter.home),
    (r'^twitter/home$',twitter.home),
    (r'^twitter/mentions$',twitter.mentions),
    (r'^twitter/messages$',twitter.messages),
)