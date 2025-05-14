from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import PostForm
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


def create_post(request):
    if request.method == "GET":
        context = {'create_post_form': PostForm()}
        return render(request, 'app/create_post_form.html', context)
    elif request.method == "POST":
        create_post_form = PostForm(request.POST)
        if create_post_form.is_valid():
            create_post_form.save()
            return redirect('home')
        else:
            return render(request, 'app/create_post_form.html', {'create_post_form': create_post_form})
