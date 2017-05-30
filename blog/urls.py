from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login_view, name = 'login'),
    url(r'^post/logout/$',views.logout_view, name = 'logout'),
    url(r'^post/register/$',views.register_view, name = 'register'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.delete_post_view, name = 'post_delete'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    
]
