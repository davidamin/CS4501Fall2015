from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^$',views.index),
	url(r'^add_vehicle$',views.add_vehicle),
	url(r'^all_cars$',views.car_list),
	url(r'^get_car/(\d+)$',views.get_car),
	url(r'^update_car/(\d+)$',views.update_car),
	url(r'^add_user$',views.add_user),
	url(r'^get_auth$',views.get_auth),
	url(r'^is_auth$',views.is_auth),
	url(r'^revoke_auth$',views.revoke_auth),
	url(r'^update_user_info/(\d+)$',views.update_user),
	url(r'^update_password/(\d+)$',views.update_password),
	url(r'^deactivate_user/(\d+)$',views.deactivate_user),
	url(r'^get_user/(\d+)$',views.get_user),
	url(r'^add_ride$',views.create_ride),
	url(r'^all_rides$',views.ride_list),
	url(r'^update_ride/(\d+)$',views.update_ride),
	url(r'^deactivate_ride/(\d+)$',views.deactivate_ride),
	url(r'^get_ride/(\d+)$',views.get_ride),
)
