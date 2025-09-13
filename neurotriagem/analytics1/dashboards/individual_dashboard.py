import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from django.conf import settings

def gerar_dashboard_individual(df, teste_id):
    df_test = df[df['id'] == teste_id]
    if df_test.empty:
        return {'error': f'ID {teste_id} não encontrado.'}

    plots_path = os.path.join(settings.BASE_DIR, 'analytics', 'static', 'analytics')
    os.makedirs(plots_path, exist_ok=True)

    resposta_cols = df_test.filter(regex=r'^tr').columns
    respostas = df_test[resposta_cols].iloc[0]

    # Gráfico de Respostas Individuais
    plt.figure(figsize=(10, 6))
    respostas.plot(kind='bar', color='skyblue')
    plt.title(f"Respostas Individuais - Teste {teste_id}")
    plt.ylabel("Resposta")
    plt.xlabel("Questões")
    plt.xticks(rotation=45)
    plt.tight_layout()
    path_resp_individual = os.path.join(plots_path, f'resp_individual_{teste_id}.png')
    plt.savefig(path_resp_individual)
    plt.close()

    # Gráfico de Contagem de Respostas
    plt.figure(figsize=(6, 4))
    respostas.value_counts().sort_index().plot(kind='bar', color='lightgreen')
    contagem = respostas.value_counts().sort_index()
    plt.title(f"Frequência de Respostas - Teste {teste_id}")
    plt.xlabel("Resposta")
    plt.ylabel("Frequência")
    plt.tight_layout()
    for i, valor in enumerate(contagem):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom')
    path_freq = os.path.join(plots_path, f'frequencia_respostas_{teste_id}.png')
    plt.savefig(path_freq)
    plt.close()

    return {
        'resp_individual': f'analytics/resp_individual_{teste_id}.png',
        'frequencia_respostas': f'analytics/frequencia_respostas_{teste_id}.png',
        'mapa_calor': f'analytics/mapa_calor_{teste_id}.png',
        'teste_id': teste_id
    }
