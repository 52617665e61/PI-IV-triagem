from django.shortcuts import render
from .models import Triagem
from .forms import TriagemForm
import joblib
import numpy as np
import os
from .loading_ml.tdah_prediction import prever_triagem

def triagem_view(request):
    resultado = None

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            # Gerar predição com ML
            resultado_ml = prever_triagem(form.cleaned_data)

            # Criar objeto Triagem (sem salvar ainda)
            instancia = form.save(commit=False)
            instancia.resultado_triagem = resultado_ml['classe']
            instancia.save()

            resultado = resultado_ml
    else:
        form = TriagemForm()

    return render(request, 'triagem/formulario.html', {'form': form, 'resultado': resultado})

