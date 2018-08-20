from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def post_view(request):
    if request.user.is_authenticated():
        context = {"title":"list"}
    else:
        context = {"title":"unlogged"} 
    return render(request, "index.html", context)
    #return HttpResponse("<h1>Post</h1>")

def put_view(request):
    queryset = Post.objects.all()
    context = {"post_list":queryset}
    return render(request, "index.html", context)
    
def delete_view(request):
    return HttpResponse("<h1>delete</h1>")

def update_view(request):
    return HttpResponse("<h1>update</h1>")