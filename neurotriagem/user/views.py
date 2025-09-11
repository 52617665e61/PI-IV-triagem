# user/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegistroUsuarioForm

def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro realizado com sucesso!')
            login(request, user)
            return redirect('home')  # Substitua por sua URL inicial
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'user/registro.html', {'form': form})
