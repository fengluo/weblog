from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import *

urlpatterns = patterns('',
    # Example:
    # (r'^weblog/', include('weblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', index),
    (r'^p/(?P<id>\d+)$',PostHandler,{'action':'get'}),
    (r'^p/new$',PostHandler,{'action':'new'}),
    (r'^p/add$',PostHandler,{'action':'add'}),
    (r'^p/del/(?P<id>\d+)$',PostHandler,{'action':'del'}),
    (r'^p/edit/(?P<id>\d+)$',PostHandler,{'action':'edit'}),
    (r'^p/update/(?P<id>\d+)$',PostHandler,{'action':'update'}),
    (r'^login$',login),
    (r'^logout$',logout),
    (r'^home$',home),
    (r'^setting$',setting),
    (r'^updatesitemeta$',setting),
)
