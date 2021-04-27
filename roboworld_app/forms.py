from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from . models import Perfil


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Usuario', min_length=4, max_length=150)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Este usuario ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Este correo electrónico ya está registrado")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas deben ser iguales")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user



'''
'''
class PerfilForm(forms.Form):
    genero = forms.CharField(label='Genero',max_length=1)
    birth_date = forms.DateField(label='Fecha de nacimiento')

    def clean_genero(self):
        genero = self.cleaned_data.get('genero')
        return genero

    def clean_birth(self):
        birth_date = self.cleaned_data.get('birth_date')
        return birth_date

    def saveDatos(self, commit=True):
        perfil = Perfil.objects.create(self.cleaned_data['genero'],self.cleaned_data['birth_date'])
        return perfil
'''
'''