import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint, uniform
import joblib

# 1. Carregando os dados
df = pd.read_excel(r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx', header=1)

tr_cols = [f"tr{i}" for i in range(1, 44)]
X = df[tr_cols]
y = df["group"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Espaço de busca com distribuições aleatórias
param_dist = {
    'n_estimators': randint(100, 350),           # número de árvores
    'learning_rate': uniform(0.01, 0.3),         # taxa de aprendizado (0.01 a 0.31)
    'max_depth': randint(3, 6),                  # profundidade da árvore
    'min_samples_split': randint(2, 6),          # mínimo para dividir
    'min_samples_leaf': randint(1, 5),           # mínimo por folha
    'subsample': uniform(0.8, 0.2)               # de 0.8 a 1.0
}

# 3. Configuração do RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=GradientBoostingClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=30,                   # experimenta 30 combinações aleatórias
    cv=5,                        # validação cruzada com 5 dobras
    scoring='f1',                # otimizar F1-score
    random_state=42,
    n_jobs=-1,                   # usar todos os núcleos disponíveis
    verbose=2
)

# 4. Treinamento
random_search.fit(X_train, y_train)

# 5. Resultados
best_model = random_search.best_estimator_
print("Melhores hiperparâmetros:", random_search.best_params_)

y_pred = best_model.predict(X_test)

print("📊 Acurácia:", accuracy_score(y_test, y_pred))
print("\n📋 Classification Report:\n", classification_report(y_test, y_pred))
print("\n🧱 Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

# 6. Salvar modelo treinado
joblib.dump(best_model, 'modelo_gradientboosting_random_search.pkl')
