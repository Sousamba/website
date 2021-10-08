from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Olá, Layla da Cruz Sousa, você vai ganhar uma viagem para os Estados Unidos no Natal')


