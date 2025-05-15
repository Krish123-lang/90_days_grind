from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'appone/index.html', context)


def create(request):
    if request.method == "GET":
        context = {'form': PostForm()}
        return render(request, 'appone/create.html', context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "Post Added Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the following errors:")
            return render(request, 'appone/create.html', {'form': form})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'appone/post_detail.html', {'post': post})


def edit(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, id=id)

    if request.method == "GET":
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'appone/create.html', context)
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.warning(request, "Post Updated Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the following errors:")
            return render(request, 'appone/create.html', {'form': form})


def delete(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    context = {'post': post}

    if request.method == "GET":
        return render(request, "appone/delete.html", context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('home')
