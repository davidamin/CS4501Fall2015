from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^$',views.view_normal),
	url(r'^ride_detail/(\d+)$',views.ride_detail),
	url(r'^login', views.login),
	url(r'^logout', views.logout),
	url(r'^create_user', views.create_user),
	url(r'^create_vehicle', views.create_vehicle),
)
