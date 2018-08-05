from django.contrib import admin
from . models import Post, Category
from . forms import PostForm

class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'created_at', 'updated_at']
    form = PostForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
