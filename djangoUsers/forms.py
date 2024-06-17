from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from djangoUsers.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'status', 'birth_date', 'city', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Электрондық пошта бұрыннан бар")

        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Пайдаланушы аты бұрыннан бар")

        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if CustomUser.objects.filter(phone=phone).exists():
            raise ValidationError("Телефон номер бұрыннан бар")

        return phone


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user