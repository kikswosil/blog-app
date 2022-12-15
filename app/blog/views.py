from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout #type: ignore
from django.contrib.auth.decorators import login_required, permission_required
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

def log_in(request):
    if request.method == 'POST':
        # handle login logic
        data = request.POST
        user = authenticate(username = data['username'], password = data['password'])
        if user is not None:
            login(request, user) # type: ignore
        return redirect('/')
    return render(request, 'login.html', {})

def log_out(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    if request.method == 'POST' and request.POST['password'] == request.POST['password_confirmation']:
        # handle sign up logic
        data = request.POST
        User.objects.create_user(data['username'], data['email'], data['password'])
        user = authenticate(username = data['username'], password = data['password'])
        if user is not None: 
            login(request, user) #type: ignore
            return redirect('/')
        return redirect('/login/')
    return render(request, 'signup.html', {})

@login_required(login_url='/login/')
@permission_required('blog.add_post', login_url='/login/')
def edit(request):
    post = Post()
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
    user_id = request.user.id
    if request.method == 'POST':
        data = request.POST;
        post = Post(
                title = data['title'],
                slug = data['slug'],
                content = data['content'],
                published = data['published'],
                author = User.objects.get(pk=user_id)
        )
        post.save()
        return redirect('/')
    return render(request, 'edit.html', {'post': post, 'options': options})


