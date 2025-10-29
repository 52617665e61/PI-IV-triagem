from django.shortcuts import render, get_object_or_404, redirect
from .models import Triagem, Teste
from user.models import NormalUser
from .forms import TriagemForm
import joblib
import numpy as np
import os
from .loading_ml.tdah_prediction import prever_triagem
from .utils import calcular_idade

def triagem_view(request, teste_nome):
    resultado = None
    teste = get_object_or_404(Teste, nome=teste_nome)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)

            # Pega a instância real (NormalUser, PsicologoUser ou AdminUser)
            usuario_real = request.user.get_real_instance()

            # Garante que é um NormalUser antes de salvar
            if isinstance(usuario_real, NormalUser):
                instancia.usuario = usuario_real
                instancia.teste = teste
                instancia.age = calcular_idade(usuario_real.born)
                instancia.gender = usuario_real.gender
            else:
                # Opcional: tratar caso o usuário não seja NormalUser
                return HttpResponseForbidden("Apenas usuários normais podem realizar triagens.")

            # Geração do resultado da ML
            dados_ml = form.cleaned_data.copy()
            dados_ml['gender'] = usuario_real.gender
            dados_ml['age'] = instancia.age
            resultado_ml = prever_triagem(dados_ml)

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

