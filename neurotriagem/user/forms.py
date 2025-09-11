# user/forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import NewUser


class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        help_text='A senha deve conter pelo menos 8 caracteres.'
    )
    password2 = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput
    )

    class Meta:
        model = NewUser
        fields = [
            'user_name', 'first_name', 'last_name', 'email',
            'data_nascimento', 'telefone', 'tipo',
            # Campos de psicólogo
            'endereco_rua', 'endereco_numero', 'bairro', 'cep',
            'cidade', 'estado', 'registro_profissional'
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não coincidem.")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')

        # Validação extra para psicólogos
        if tipo == 'psicologo':
            required_fields = [
                'endereco_rua', 'endereco_numero', 'bairro',
                'cep', 'cidade', 'estado', 'registro_profissional'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, 'Este campo é obrigatório para psicólogos.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
