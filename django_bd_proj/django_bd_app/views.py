from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos de idade!</h1>'.format(nome, idade))

def soma(request, num1, num2):
    total = num1 + num1
    return HttpResponse('<h2>A soma de {} com {} é igual a: {}</h2>'.format(num1, num2, total))