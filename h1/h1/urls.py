from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^first/', include('first.urls')),
    url(r'^view/', include('third.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^exp/', include('second.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
