from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^ride_detail/(\d+)$',views.ride_detail),
	url(r'^home_detail/$',views.home_detail),
	url(r'^create_user/$',views.create_user),
)
