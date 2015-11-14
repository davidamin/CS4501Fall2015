from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^ride_detail/(\d+)$',views.ride_detail),
	url(r'^home_detail/$',views.home_detail),
	url(r'^create_user/$',views.create_user),
	url(r'^login/$',views.login),
	url(r'^logout/$',views.logout),
	url(r'^create_ride/$',views.add_new_ride),
	url(r'^create_vehicle/$', views.add_new_vehicle),
	url(r'^search/$', views.search_result),
)
