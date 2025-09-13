import joblib

_model = joblib.load('C:\Users\USER\Desktop\PI-4\neurotriagem\ml\modelo_tdah.pkl')

def prever_paciente(dados_paciente):
    return _model.predict([dados_paciente])
