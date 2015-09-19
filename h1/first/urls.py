from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^$',views.index),
	url(r'^add_vehicle$',views.add_vehicle),
	url(r'^all_cars$',views.car_list),
	url(r'^get_car/(\d+)$',views.get_car),
	url(r'^update_car/(\d+)$',views.update_car),
)
