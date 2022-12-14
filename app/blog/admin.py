from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User
# Register your models here.

class PostForm(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'published', 'author']

admin.site.register(Post)
