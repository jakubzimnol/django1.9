from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'post is created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'post is not created')

    #if request.method == "POST":
    #    print(request.POST.get("text"))
    return render(request, "post_create.html", context)


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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    context = {"form":form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a>Saved!", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
        
    return render(request, "post_create.html", context)