import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# 1. Carregando os dados
df = pd.read_excel(r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx', header=1)

tr_cols = [f"tr{i}" for i in range(1, 44)]
X = df[tr_cols]
y = df["group"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Definindo o espaço de busca para hiperparâmetros
param_grid = {
    'n_estimators': [100, 200, 300],       # número de árvores
    'learning_rate': [0.01, 0.1, 0.2],     # taxa de aprendizado
    'max_depth': [3, 4, 5],                # profundidade máxima
    'min_samples_split': [2, 5],           # mínimo para dividir um nó
    'min_samples_leaf': [1, 2, 4],         # mínimo em uma folha
    'subsample': [0.8, 1.0]                # proporção de amostras para cada árvore
}

# 3. Configurando GridSearchCV
grid_search = GridSearchCV(
    estimator=GradientBoostingClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='f1',  # f1-score para equilibrar precisão e recall
    verbose=2,
    n_jobs=-1
)

# 4. Treinando o modelo com busca de hiperparâmetros
grid_search.fit(X_train, y_train)

# 5. Resultados
best_model = grid_search.best_estimator_
print("Melhores hiperparâmetros:", grid_search.best_params_)

y_pred = best_model.predict(X_test)
print("📊 Acurácia:", accuracy_score(y_test, y_pred))
print("\n📋 Classification Report:\n", classification_report(y_test, y_pred))
print("\n🧱 Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

# 6. Salvar modelo
joblib.dump(best_model, 'modelo_gradientboosting_otimizado.pkl')
