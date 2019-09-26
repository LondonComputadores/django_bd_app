from django.shortcuts import render, HttpResponse  #redirect
from django_bd_app.models import Evento

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos de idade!</h1>'.format(nome, idade))

def soma(request, num1, num2):
    total = num1 + num1
    return HttpResponse('<h2>A soma de {} com {} é igual a: {}</h2>'.format(num1, num2, total))

def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #get(id=1) foi substituido por .all() e .all() por filter(usuario=...)
    dados = {'eventos':evento}    #response foi subtituido por dados
    return render(request, 'agenda.html', dados)