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
        return render(request=request, template_name="lecture/lecture.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_page)

        return render(request=request, template_name="lecture/lecture.html",
                      context={"error": "Пайдаланушы атыңыз және/немесе құпия сөзіңіз дұрыс емес.",
                               'user': request.user})


class PrintInputView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture1-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElseView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture2-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class CalculationsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture3-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoopView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture4-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class StrView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture5-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoopView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture6-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture7-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class FunctionView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture8-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ArrayView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture9-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class SetsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture10-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class DictionaryView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture11-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)
