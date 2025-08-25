from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = '__all__'
        exclude = ['resultado_triagem', 'data_envio']