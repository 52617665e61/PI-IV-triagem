from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def lista_de_servicos(request):
    return render(request, 'pages/lista_de_servicos.html')

def quem_somos(request):
    return render(request, 'pages/quem_somos.html')