from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from .models import Thread

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("posts")
    return render(request, "login.html", {"request": request})  

def login_auth(request):
    return redirect("posts")


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "my_posts.html", {"posts": posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post": post})

@login_required
def create_post(request):
    threads = Thread.objects.all()  
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form, 'threads': threads})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect("posts")
    return redirect("post_detail", id=id)
