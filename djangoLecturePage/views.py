from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from djangoMainPage.models import Lecture

# Create your views here.
def lecture(request):
    context = {
        'lecture': Lecture.objects.values_list()[0],
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

    return render(request=request, template_name="lecture/task.html", context={"error": "Invalid Credentials", 'user':request.user})