from django.shortcuts import render
from urllib import request
from django.conf import settings
from analytics.dashboards import modelo_dashboard, geral_dashboard, individual_dashboard

from triagem.models import Triagem
import pandas as pd

def dashboard_modelo(request):
    modelo = modelo_dashboard.carregar_modelo()
    df = pd.read_excel(r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx', header=1)
    df = df.dropna(subset=['group'])
    
    features = ['gender', 'age', 'nsc'] + [f"tr{i}" for i in range(1, 44)] + [f"demo{i}" for i in range(1, 27)]
    df = df.dropna(subset=features)
    
    X = df[features]
    y = df['group']

    modelo_dashboard.importancia_features(modelo, features)
    modelo_dashboard.gerar_matriz_confusao(modelo, X, y)
    relatorio = modelo_dashboard.gerar_relatorio_classificacao(modelo, X, y)

    return render(request, 'analytics/modelo_dashboard.html', {
        'relatorio': relatorio
    })

def dashboard_geral(request):
    registros = Triagem.objects.all().values()
    df = pd.DataFrame(registros)
    paths = geral_dashboard.gerar_dashboard_geral(df)
    return render(request, 'analytics/geral_dashboard.html', paths)

def dashboard_individual(request, teste_id):
    registros = Triagem.objects.all().values()
    df = pd.DataFrame(registros) 
    paths = individual_dashboard.gerar_dashboard_individual(df, teste_id)

    # Caso o teste_id não exista
    if 'error' in paths:
        pass
 
    return render(request, 'analytics/individual_dashboard.html', paths)
