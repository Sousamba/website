from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Olá, Carla Gomes da Silva,  Em breve teremos novidades' )

