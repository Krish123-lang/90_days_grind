from django.shortcuts import render
from .forms import LoginForm

# Create your views here.


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
