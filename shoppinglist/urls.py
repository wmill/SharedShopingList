from django.conf.urls import patterns, url

from shoppinglist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)