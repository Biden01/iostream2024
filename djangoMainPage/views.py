from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect


def home(request: HttpRequest):
    if request.method == "GET":
        return render(request=request, template_name="main/main.html", context={'user':request.user})

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("main")
    context = {
        "error": "Пайдаланушы атыңыз және/немесе құпия сөзіңіз дұрыс емес.",
        'user': request.user
    }

    return render(request=request, template_name="main/main.html", context=context)


def logoutProfile(request: HttpRequest):
    logout(request=request)
    return redirect("/")