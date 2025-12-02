from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import BlogForm
from .models import BlogModel
from django.contrib import messages

# Create your views here.

def home(request):
    posts=BlogModel.objects.all()
    context={
        "posts": posts,
        "title": "The zen of python",    }
    return render(request, "blog/home.html", context)

def create_post(request):
    if request.method == "GET":
        form=BlogForm()
        return render(request, "blog/create_post.html", {'form': form})
    elif request.method == "POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong!")
            return render(request, "blog/create_post.html", {"form": form})

def edit_post(request, id):
    posts=get_object_or_404(BlogModel, id=id)
    if request.method == "GET":
        context={"form": BlogForm(instance=posts), 'id':id}
        return render(request, "blog/create_post.html", context)
    elif request.method == "POST":
        form=BlogForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong!")
            return render(request, "blog/create_post.html", {"form": form})
    
def about(request):
    return render(request, "blog/about.html")