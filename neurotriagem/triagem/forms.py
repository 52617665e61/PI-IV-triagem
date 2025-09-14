from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = '__all__'
        exclude = ['usuario', 'teste', 'age', 'gender', 'resultado_ml', 'probabilidades_ml',
                   'data_envio', 'psicologo_revisor', 'revisado', 'comentario_revisor', 'data_revisao']