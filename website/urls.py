
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.get_home_page),
	url(r'^getdailymenu/$', views.get_daily_menu),
]
