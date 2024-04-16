from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants, add_message
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')
        users = User.objects.filter(username=username)
    if users.exists():
        add_message(request, constants.ERROR, 'Usuário já existe')
        return redirect('/usuarios/cadastro')
    if senha != confirmar_senha:
        add_message(request, constants.ERROR, 'A senha e o confirmar senha devem ser iguais')
        return redirect('/usuarios/cadastro')
    if len(senha) < 6:
        add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
        return redirect('/usuarios/cadastro')

    try:
        User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        return redirect('/usuarios/login')
    except:
        add_message(request, constants.ERROR, 'Erro ao realizar cadastro. Tente novamente!')
        return redirect('/usuarios/cadastro')
    
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")
        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')
        add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')

def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')