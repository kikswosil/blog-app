from django.shortcuts import get_object_or_404, render
from .models import Post

PUBLISHED = 1
DRAFT = 0

def index(request):
    posts = Post.objects.filter(published=PUBLISHED) or [] #type: ignore
    return render(request, 'main.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, published=PUBLISHED)
    return render(request, 'post.html', {'post': post})
