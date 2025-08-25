import joblib
import numpy as np
import os

# Caminho absoluto ao arquivo .pkl
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
MODEL_PATH = os.path.join(BASE_DIR, 'modelo_tdha.pkl')

model = joblib.load(MODEL_PATH)

def prever_triagem(dados_dict):
    """
    Recebe um dicionário com os campos tr1 a tr43 e retorna classe e probabilidade.
    """
    dados = []
    for i in range(1, 44):
        key = f'tr{i}'
        dados.append(int(dados_dict[key]))
    
    dados_np = np.array(dados).reshape(1, -1)

    pred = model.predict(dados_np)
    prob = model.predict_proba(dados_np)

    return {
        'classe': int(pred[0]),
        'probabilidade': float(prob[0][int(pred[0])])
    }
