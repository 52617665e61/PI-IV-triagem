import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.conf import settings

def gerar_dashboard_geral(df):
    plots_path = os.path.join(settings.BASE_DIR, 'analytics', 'static', 'analytics')
    os.makedirs(plots_path, exist_ok=True)

    # Histograma de idade
    plt.figure(figsize=(8, 5))
    df['age'].hist(bins=20)
    plt.title("Distribuição de Idade")
    plt.xlabel("Idade")
    plt.ylabel("Frequência")
    plt.tight_layout()
    hist_path = os.path.join(plots_path, 'hist_idade.png')
    plt.savefig(hist_path)
    plt.close()

    # Média por gênero
    plt.figure(figsize=(6, 4))
    df.groupby('gender')['age'].mean().plot(kind='bar')
    plt.title("Idade Média por Gênero")
    plt.ylabel("Idade Média")
    plt.tight_layout()
    bar_path = os.path.join(plots_path, 'media_idade_genero.png')
    plt.savefig(bar_path)
    plt.close()

    return {
        'hist_idade': 'analytics/hist_idade.png',
        'media_idade_genero': 'analytics/media_idade_genero.png'
    }
