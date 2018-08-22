from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {"queryset": queryset,
              "title": "List",
              'page_request_var': page_request_var}
    return render(request, "post_list.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()    
    messages.success(request, "deleted success")
    return redirect("posts:list")


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