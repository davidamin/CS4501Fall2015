from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
	url(r'^$',views.index),
	url(r'^add_vehicle$',views.add_vehicle)
)