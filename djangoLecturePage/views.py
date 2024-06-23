from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from djangoMainPage.models import Lecture
from django.views import View

redirect_page = 'main'


class LecturePageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'lecture': Lecture.objects.values_list(),
            'user': request.user
        }
        return render(request=request, template_name="lecture/task.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_page)

        return render(request=request, template_name="lecture/task.html",
                      context={"error": "Пайдаланушы атыңыз және/немесе құпия сөзіңіз дұрыс емес.",
                               'user': request.user})


class PrintInputView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/task1-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)
