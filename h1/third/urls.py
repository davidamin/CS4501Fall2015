from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^$',views.view_normal),
	url(r'^ride_detail/(\d+)$',views.ride_detail),
	url(r'^login', views.login),
	url(r'^logout', views.logout),
)
