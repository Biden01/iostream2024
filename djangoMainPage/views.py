from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="main/main.html", context={'user': request.user})

    def post(self, request):
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


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect("/")