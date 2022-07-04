import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import password_is_valid


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro/')
        
        return HttpResponse(f'Usuraio: {usuario} - Email: {email} - Senha: {senha} - Confirmar Senha: {confirmar_senha}')
    
def logar(request):
    return HttpResponse('Logar')