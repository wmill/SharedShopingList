from django.conf.urls import patterns, url

from shoppinglist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^update$', views.update, name='update'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^accounts/login/?$', views.login_view, name='login'),

)