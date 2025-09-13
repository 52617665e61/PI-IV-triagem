from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import  RegistroUsuarioNormalForm, RegistroUsuarioPsicologoForm, RegistroUsuarioAdminForm
from .models import PsicologoUser, AdminUser, NormalUser

# views.py

def registro_escolha_view(request):
    # Página inicial com os dois cards
    return render(request, 'user/registro_escolha.html')


def register_view(request, tipo):
    # Recebe o tipo pela URL
    form_class_map = {
        'normal': RegistroUsuarioNormalForm,
        'psicologo': RegistroUsuarioPsicologoForm,
        'admin': RegistroUsuarioAdminForm,
    }

    form_class = form_class_map.get(tipo)
    if not form_class:
        messages.error(request, 'Tipo de registro inválido.')
        return redirect('registro_escolha')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro realizado com sucesso!')
            login(request, user)
            return redirect('pages:index')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = form_class()

    return render(request, 'user/registro_formulario.html', {
        'form': form,
        'tipo_selecionado': tipo,
    })


class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        real_user = self.request.user.get_real_instance()

        if isinstance(real_user, PsicologoUser):
            return reverse_lazy('index')
        elif isinstance(real_user, AdminUser):
            return reverse_lazy('index')
        elif isinstance(real_user, NormalUser):
            return reverse_lazy('pages:index')

        return reverse_lazy('pages:index')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

