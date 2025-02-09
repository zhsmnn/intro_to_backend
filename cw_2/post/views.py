from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list_create')
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'form': form})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('tadas')
    return render(request, 'post_confirm_delete.html', {'post': post})

def tadas(request):
    return render(request, 'tadas.html')

def home(request):
    return render(request, 'home.html')