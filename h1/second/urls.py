from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^ride_detail/(\d+)$',views.ride_detail),
)
