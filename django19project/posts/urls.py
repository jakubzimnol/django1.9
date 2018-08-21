from django.conf.urls import url
#from posts import views

urlpatterns = [
    url(r'^$', "posts.views.post_list", name ='list'),
    url(r'^create/$', "posts.views.post_create", name='create'),
    url(r'^(?P<id>\d+)/edit/$', "posts.views.post_update", name='update'),
    url(r'^(?P<id>\d+)/delete/$', "posts.views.post_delete", name='delete'),
    url(r'^(?P<id>\d+)/$', "posts.views.post_detail", name='detail'),
]
