from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	#url(r'^$',views.index),
	url(r'^ride_detail$',views.ride_detail),
)
