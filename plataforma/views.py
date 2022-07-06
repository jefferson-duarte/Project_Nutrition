from django.http import HttpResponse
from django.shortcuts import render

def pacientes(request):
    return HttpResponse('Pacientes')