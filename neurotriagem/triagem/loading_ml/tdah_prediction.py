import joblib
import numpy as np
import os


# Path do modelo treinado
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(BASE_DIR, 'ml', 'modelo_tdah2.pkl')

# Loading model 
model = joblib.load(MODEL_PATH)

def prever_triagem(dados_dict):
    dados = []

    dados.append(int(dados_dict['gender']))
    dados.append(int(dados_dict['age']))
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
