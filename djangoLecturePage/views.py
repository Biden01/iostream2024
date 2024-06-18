from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from djangoMainPage.models import Lecture
from djangoUsers.models import CustomUser

redirect_page = 'main'


def lecture(request):
    context = {
        'lecture': Lecture.objects.values_list(),
        'user': request.user
    }
    if request.method == "GET":
        return render(request=request, template_name="lecture/task.html", context=context)

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/lecture/")

    return render(request=request, template_name="lecture/task.html", context={"error": "Пайдаланушы атыңыз және/немесе құпия сөзіңіз дұрыс емес.", 'user':request.user})

def print_input(request):
    return render(request=request, template_name='lecture/task1-1.html', context={})