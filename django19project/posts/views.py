from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def post_create(request):
    if request.user.is_authenticated():
        context = {"title":"list"}
    else:
        context = {"title":"unlogged"} 
    return render(request, "index.html", context)
    #return HttpResponse("<h1>Post</h1>")

def post_detail(request, id=None):
    #instatnce = Post.objects.get_object_or_404(id=5)
    instance = get_object_or_404(Post, id=id)
    context = {"title":"detail",
               "instance":instance}
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {"post_list":queryset}
    return render(request, "index.html", context)
    
def post_delete(request):
    return HttpResponse("<h1>delete</h1>")

def post_update(request):
    return HttpResponse("<h1>update</h1>")