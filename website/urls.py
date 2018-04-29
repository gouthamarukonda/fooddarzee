
from django.conf.urls import url
from . import views, views2

urlpatterns = [
	url(r'^$', views.get_home_page),
]
