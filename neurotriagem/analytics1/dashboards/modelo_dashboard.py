import joblib
import pandas as pd
import matplotlib
matplotlib.use('Agg') #Sem isso quando gera imagem ele tenta gerar via GUI
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import os
from django.conf import settings

MODELO_PATH = os.path.join("modelo_tdah.pkl")
output_path = os.path.join(
    settings.BASE_DIR, 
    'analytics', 
    'static',
    'analytics', 
)


def carregar_modelo():
    return joblib.load(MODELO_PATH)

def importancia_features(modelo, feature_names):
    importancias = modelo.feature_importances_
    df = pd.DataFrame({'feature': feature_names, 'importancia': importancias})
    df = df.sort_values('importancia', ascending=False)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='importancia', y='feature', data=df.head(20))
    plt.title("Top 20 Features Mais Importantes")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "importancia_features.png"))
    plt.close()

    return df

def gerar_matriz_confusao(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Matriz de Confusão")
    plt.xlabel("Predito")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "matriz_confusao.png"))
    plt.close()

    return cm

def gerar_relatorio_classificacao(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    relatorio = classification_report(y_test, y_pred, output_dict=True)
    return pd.DataFrame(relatorio).T
