from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^models/', include('first.urls')),
    url(r'^exp/', include('second.urls')),
    url(r'^v1/', include('third.urls')),
    url(r'', include('third.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
