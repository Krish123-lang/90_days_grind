from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BlogForm
from .models import BlogModel

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
            return redirect('home')
        else:
            return render(request, "blog/create_post.html", {"form": form})

def about(request):
    return render(request, "blog/about.html")