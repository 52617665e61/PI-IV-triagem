# treinar_modelo.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

tr_cols = ['gender', 'age',	'nsc'] + [f"tr{i}" for i in range(1, 44)]  + [f"demo{1}" for i in range(1, 27)]
print(tr_cols)
# 1. Carregar o ESM3 (já limpo)
df = pd.read_excel(r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx', header=1)

# 2. Definir variáveis explicativas (features) e alvo (target)
# Selecionando tr1 até tr43

X = df[tr_cols]
y = df["group"]

# 3. Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Previsão e avaliação
y_pred = model.predict(X_test)

print(" Acurácia:", accuracy_score(y_test, y_pred))
print("\n Classification Report:\n", classification_report(y_test, y_pred))



# 7. Importância das variáveis
importances = pd.Series(model.feature_importances_, index=tr_cols)
importances.nlargest(10).plot(kind='barh', color='skyblue')
plt.title(" Top 10 Features Mais Importantes")
plt.xlabel("Importância")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

joblib.dump(model, 'modelo_tdha.pkl')

