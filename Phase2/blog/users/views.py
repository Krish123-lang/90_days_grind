from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")

        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)

    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f"Hi, {username.title()}, welcome back")
                return redirect("home")

        messages.error(request, "Invalid username or password!")
        return render(request, "users/login.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("login")


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Signed In successfully!")
            login(request, user)
            return redirect("home")
        else:
            return render(request, "users/register.html", {"form": form})
