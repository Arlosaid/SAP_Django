from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Adios, hasta pronto')

def contacto(request):
    return HttpResponse('Correo: adroal08@gmail.com\ntelefono:6251043989')
