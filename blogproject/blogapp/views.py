from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as auth_logout


def registration(request: HttpRequest) -> HttpResponse:
    """View for user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {"form": form})


def login(request: HttpRequest) -> HttpResponse:
    """View for user login."""
    if request.method == "POST":
        username: str = request.POST["username"]
        password: str = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message: str = "Invalid username or password."
            return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")


def logout(request: HttpRequest) -> HttpResponse:
    """View for user logout."""
    auth_logout(request)
    # return redirect("/")
    return render(request, 'logout.html')

