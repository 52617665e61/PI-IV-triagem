from django.shortcuts import render
from .models import Triagem
from .forms import TriagemForm
import joblib
import numpy as np
import os
from .loading_ml.tdah_prediction import prever_triagem


# Carregar o modelo treinado (coloque o caminho correto do seu arquivo .pkl)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(BASE_DIR, 'modelo_tdha.pkl')
model = joblib.load(MODEL_PATH)
'''
def triagem_tdh(request):
    resultado = None
    if request.method == 'POST':
        form = TriagemTDAHForm(request.POST)
        if form.is_valid():
            # Extrair os dados do formulário e criar array numpy para o modelo
            dados = []
            for i in range(1, 44):  # se forem 43 perguntas tr1..tr43
                key = f'tr{i}'
                dados.append(form.cleaned_data[key])
            dados = np.array(dados).reshape(1, -1)

            # Fazer a previsão
            pred = model.predict(dados)
            prob = model.predict_proba(dados)

            resultado = {
                'classe': int(pred[0]),
                'probabilidade': prob[0][int(pred[0])]
            }
    else:
        form = TriagemTDAHForm()

    return render(request, 'triagem/formulario.html', {'form': form, 'resultado': resultado})

from django.shortcuts import render, redirect'''

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

