from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogModel

# Create your views here.

def home(request):
    posts=BlogModel.objects.all()
    context={
        "posts": posts,
        "title": "The zen of python",    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")