from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.shortcuts import render, redirect


class Register(View):

    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        context = {
            'form': form,
            'error': "Пайдаланушы атыңыз және/немесе құпия сөзіңіз дұрыс емес.",
        }
        return render(request, self.template_name, context)