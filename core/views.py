from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse("<h1>Hello World! Bem vindo {}, você tem {}</h1>".format(nome, idade))
