from django.shortcuts import render, HttpResponse, redirect
from django_bd_app.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos de idade!</h1>'.format(nome, idade))

def soma(request, num1, num2):
    total = num1 + num1
    return HttpResponse('<h2>A soma de {} com {} é igual a: {}</h2>'.format(num1, num2, total))

def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')  #pass foi substituido pelo codigo atual
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou Senha inválido. Tente novamente!')
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #get(id=1) foi substituido por .all() e .all() por filter(usuario=...)
    dados = {'eventos':evento}    #response foi subtituido por dados
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def eventos(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')