from django.conf.urls import url
from . import views
from .views import post_detail, post_new, post_list
urlpatterns = [
    url(r'post/new/', post_new, name='post_new'),
    url(r'post/(?P<pk>[0-9]+)/', post_detail, name='post_detail'),
    url(r'post/list', post_list, name='post_list'),
    url(r'post/edit/(?P<pk>[0-9]+)/', views.post_edit, name='post_edit'),

]