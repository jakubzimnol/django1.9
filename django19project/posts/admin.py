from django.contrib import admin
from posts.models import Post

# Register your models here.

class AdminModelPost(admin.ModelAdmin):
    #fieldsets = ['title','created','updated']
    list_display = ('title','created','updated')
    list_display_links = ('created','updated')
    list_filter = ('created','updated')
    list_editable = ['title']
    search_fields = ['title','text']
    class Meta:
        model=Post

admin.site.register(Post, AdminModelPost)