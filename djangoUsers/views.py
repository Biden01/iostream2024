from django.contrib.auth import authenticate, login
from djangoUsers.forms import CustomUserCreationForm
from django.views.generic import View
from django.shortcuts import render, redirect


class Register(View):

    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('main')
        context = {
            'form': form,
            'error': form.errors,
        }
        return render(request, self.template_name, context)
