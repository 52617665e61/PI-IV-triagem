from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro realizado com sucesso!')
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'user/registro.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.tipo == 'normal':
            return reverse_lazy('index')
        elif user.tipo == 'psicologo':
            return reverse_lazy('index')
        elif user.tipo == 'admin':
            return reverse_lazy('index') 
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

