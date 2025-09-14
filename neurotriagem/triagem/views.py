from django.shortcuts import render, get_object_or_404, redirect
from .models import Triagem, Teste
from .forms import TriagemForm
import joblib
import numpy as np
import os
from .loading_ml.tdah_prediction import prever_triagem
from .utils import calcular_idade

def triagem_view(request, teste_nome):
    resultado = None
    teste = get_object_or_404(Teste, nome= teste_nome)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.usuario = request.user
            instancia.teste = teste
            instancia.age = calcular_idade(request.user.born)
            instancia.gender = request.user.gender

            # Geração do resultado da ML
            resultado_ml = prever_triagem(form.cleaned_data)
            instancia.resultado_ml = resultado_ml['classe']
            instancia.probabilidades_ml = resultado_ml.get('probabilidades')
            instancia.save()

            resultado = resultado_ml
    else:
        form = TriagemForm()

    return render(request, 'triagem/formulario.html', {
        'form': form,
        'resultado': resultado,
        'teste': teste
    })

