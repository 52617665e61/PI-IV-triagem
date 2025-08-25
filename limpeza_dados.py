import pandas as pd

# 1. Carregar os dados (mude o caminho para o seu arquivo)
df = pd.read_excel(r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx', header=1)

# 2. Visualizar as primeiras linhas para entender a estrutura
print("Primeiras linhas do dataset:")
print(df.head())

# 3. Verificar tipos de dados
print("\nTipos de dados antes da conversão:")
print(df.dtypes)

# 4. Ajustar tipos de dados se necessário (exemplo: idade para int)
if df['age'].dtype != 'int64':
    df['age'] = df['age'].fillna(0).astype(int)  # Exemplo simples

# 5. Verificar valores faltantes
print("\nContagem de valores faltantes por coluna:")
print(df.isnull().sum())

# 6. Decidir o que fazer com valores faltantes
# Exemplo: remover linhas com valores faltantes
df = df.dropna()

# 7. Verificar duplicatas
print("\nNúmero de duplicatas no dataset:", df.duplicated().sum())

# 8. Remover duplicatas, se existirem
df = df.drop_duplicates()

# 9. Padronizar nomes das colunas (opcional, exemplo: tudo minúsculo)
df.columns = [col.lower() for col in df.columns]

# 10. Salvar o dataset limpo
df.to_csv(r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM_limpo.csv', index=False)
print("\nArquivo limpo salvo com sucesso!")

