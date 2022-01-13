from django import forms

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):

    #Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    last_name = forms.CharField()
    first_name = forms.CharField()

class Meta:
    model = User
    fields = [ 'email', 'password1', ' password2', 'first_name', 'last_name'] 
        
    
    
# class Meta:
#     model = User
#     fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
    # # Saca los mensajes de ayuda
    # help_texts = {k:"" for k in fields}






class UserRegisterForm(UserCreationForm):

    #Requisitos indispensables
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    #Requisitos extras
    last_name = forms.CharField()
    first_name = forms.CharField()

    #imagen_avatar = forms.ImageField(required=False)



    
# class Meta:
#     model = User
#     fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        
#     # help_texts = {k:"" for k in fields}




class VenderFormulario(forms.Form):

    
    marca = forms.CharField(max_length=40) 
    modelo = forms.CharField(max_length=40)
    anio = forms.IntegerField()

class MotoFormulario(forms.Form):

    marca = forms.CharField(max_length=40) 
    modelo = forms.CharField(max_length=40)
    anio = forms.IntegerField()

class CamionFormulario(forms.Form):

    marca = forms.CharField(max_length=40) 
    modelo = forms.CharField(max_length=40)
    anio = forms.IntegerField()
