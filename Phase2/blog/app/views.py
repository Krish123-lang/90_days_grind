from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
'''
posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]
'''


def home(request) -> HttpResponse:
    posts = Post.objects.all()
    context = {'posts': posts, 'title': 'Django is amazing'}
    return render(request, 'app/index.html', context)


def about(request):
    return render(request, 'app/about.html')
