import joblib
import numpy as np
import os
import pandas as pd

import matplotlib.pyplot as plt

# Caminho para os arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'modelo_tdha.pkl')


# Carrega modelo e scaler
model = joblib.load(MODEL_PATH)


# --------------------------
# Simular dados de entrada:
# Exemplo: [idade, genero, pergunta_1, ..., pergunta_n]
# Deve ter o mesmo número e ordem que usou no treinamento
entrada = [
    15,     # idade
    1,      # gênero (1 = masculino, 0 = feminino, por ex)
    2, 3, 1, 0, 1, 2, 3, 2,
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,2,3,4,
    5,2,3,1,4,2,3,4,5,1,
      1,1,1  # perguntas 1–9 (substitua pela quantidade real)
    # ... continue até o total exato de features usadas no treinamento
]

# Transformar para array e escalar
entrada_np = np.array([entrada])  # 2D array


# Fazer previsão
predicao = model.predict(entrada_np)[0]
proba = model.predict_proba(entrada_np)[0]

# Resultado
classe = 'TDAH' if predicao == 1 else 'Controle'
confiança = proba[predicao]

print(f"\n🧠 Previsão: {classe}")
print(f"🔍 Confiança: {confiança:.2%}")

colunas = ['idade', 'genero', 'q1', 'q2', '4','5','6','7','8','9','10','11','12','13','q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42']

# Importância das features
importancias = model.feature_importances_

# Criar um DataFrame para visualização
df_importancia = pd.DataFrame({
    'feature': colunas,
    'importance': importancias
})

# Ordenar pelo impacto (decrescente)
df_importancia = df_importancia.sort_values(by='importance', ascending=False)

print(df_importancia)

# Plotar gráfico de barras
plt.figure(figsize=(12,6))
plt.bar(df_importancia['feature'], df_importancia['importance'])
plt.xticks(rotation=90)
plt.title('Importância das Features - Random Forest')
plt.show()