from django.shortcuts import render
from .models import Usuario

def usuario(request):
    return render(request, 'usuario/usuario.html')

def base(request):
    return render(request, 'usuario/base.html')

def produtos(request):
    return render(request, 'usuario/produtos.html')




