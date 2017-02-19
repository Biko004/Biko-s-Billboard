from django.conf.urls import url

from . import views

urlpatterns = [

url(R'^$', views.index, name='index'),
url(R'^[0-9]+$', views.delete_post, name='delete post'),
url(R'^newpost$', views.newpost, name='new post'),
url(R'^newcomment$', views.newcomment, name='new comment')
]