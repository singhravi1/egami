from django.conf.urls import url
from . import views

app_name = 'img'
urlpatterns = [

		url(r'^$', views.index, name = 'index'),
		url(r'^new$', views.new, name='new'),
		url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
  ]