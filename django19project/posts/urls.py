from django.conf.urls import url
#from posts import views

urlpatterns = [
    url(r'^', "posts.views.put_view"),
    url(r'^create/$', "posts.views.post_view"),
    url(r'^put/$', "posts.views.put_view"),
    url(r'^update/$', "posts.views.update_view"),
    url(r'^delete/$', "posts.views.delete_view"),
]
