import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import joblib

# ========== Funções do Pipeline de Treinamento ==========

def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset Excel com os dados de triagem.
    """
    df = pd.read_excel(caminho_arquivo, header=1)
    return df


def preprocessar_dados(df):
    """
    Faz pré-processamento: tratamento de nulos e balanceamento de classes.
    """
    tr_cols = ['gender', 'age'] + [f"tr{i}" for i in range(1, 44)]
    # Remove linhas com valores nulos nas colunas essenciais
    df = df.dropna(subset=tr_cols + ['group'])

    X = df[tr_cols]
    y = df['group']

    # Balanceia as classes usando SMOTE
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X, y)

    return X_res, y_res, tr_cols


def ajustar_modelo(X, y):
    """
    Ajusta o modelo RandomForest com GridSearchCV para encontrar os melhores hiperparâmetros.
    """
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'bootstrap': [True, False]
    }

    rf = RandomForestClassifier(random_state=42)
    grid = GridSearchCV(rf, param_grid, cv=5, scoring='f1_macro', n_jobs=-1, verbose=2)
    grid.fit(X, y)

    return grid.best_estimator_, grid.best_params_, grid.best_score_


def avaliar_modelo(modelo, X, y):
    """
    Avalia o modelo com cross-validation e imprime métricas detalhadas.
    """
    scores = cross_val_score(modelo, X, y, cv=5, scoring='f1_macro')
    print(f"F1 Score médio (CV 5-fold): {scores.mean():.4f}")

    # Divisão treino/teste para métricas detalhadas
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))


def salvar_modelo(modelo, nome_arquivo):
    """
    Salva o modelo treinado com joblib.
    """
    joblib.dump(modelo, nome_arquivo)
    print(f"Modelo salvo como: {nome_arquivo}")


# ========== Execução do Pipeline ==========

if __name__ == "__main__":
    CAMINHO_ARQUIVO = r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx'
    MODELO_SAIDA = 'modelo_tdah.pkl'

    df = carregar_dados(CAMINHO_ARQUIVO)
    X, y, features = preprocessar_dados(df)
    modelo, melhores_parametros, melhor_score = ajustar_modelo(X, y)

    print("Melhores parâmetros encontrados:", melhores_parametros)
    print("Melhor F1 (validação):", melhor_score)

    avaliar_modelo(modelo, X, y)
    salvar_modelo(modelo, MODELO_SAIDA)
