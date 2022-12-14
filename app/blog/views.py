from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Post

PUBLISHED = 1
DRAFT = 0

def index(request):
    posts = Post.objects.filter(published=PUBLISHED) or [] #type: ignore
    return render(request, 'main.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, published=PUBLISHED)
    return render(request, 'post.html', {'post': post})

def search(request):
    query = request.GET.get('query')

    posts = Post.objects.all() #type: ignore
    result_list = []
    for post in posts:
        if post.text_matches_any(query):
            result_list.append(post)
        
    return render(request, 'search.html', {'query': query, 'posts': result_list})

def login(request):
    return render(request, 'login.html', {})

def sign_up(request):
    return render(request, 'signup.html', {})

def edit(request):
    post = Post()
    users = User.objects.all()
    options = [
        {
            'name': 'publihed',
            'value': PUBLISHED
        },
        {
            'name': 'draft',
            'value': DRAFT
        }
    ]
    if request.method == 'POST':
        # # handle post insert.
        data = request.POST;
        post = Post(
                title = data['title'],
                slug = data['slug'],
                content = data['content'],
                published = data['published'],
                author = User.objects.get(pk=data['author'])
        )
        post.save()
        # post.title = data['title']
        # post.slug = data['slug']
        # post.content = data['content']
        # post.published = data['published']
        # post.author = User.objects.get_object_or_404(pk=data['author'])
        # Post.objects.create( #type: ignore
        #         title = data['title'],
        #         slug = data['slug'],
        #         content = data['content'],
        #         publihed = data['publihed'],
        #         author = User.objects.get_object_or_404(pk=data['author'])
        # )
        return redirect('/');
    return render(request, 'edit.html', {'post': post, 'users': users, 'options': options})


