from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NormalUser, PsicologoUser, AdminUser


class RegistroUsuarioNormalForm(UserCreationForm):
    class Meta:
        model = NormalUser
        fields = [
            'email',
            'user_name',
            'first_name',
            'last_name',
            'data_nascimento',
            'telefone',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class RegistroUsuarioPsicologoForm(UserCreationForm):
    class Meta:
        model = PsicologoUser
        fields = [
            'email',
            'user_name',
            'first_name',
            'last_name',
            'data_nascimento',
            'telefone',
            'registro_profissional',
            'endereco_rua',
            'endereco_numero',
            'bairro',
            'cep',
            'cidade',
            'estado',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
    from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdminUser


class RegistroUsuarioAdminForm(UserCreationForm):
    cargo = forms.CharField(required=False, label="Cargo (opcional)")

    class Meta:
        model = AdminUser
        fields = [
            'email',
            'user_name',
            'first_name',
            'last_name',
            'cargo',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

