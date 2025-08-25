import pandas as pd

# Definir os caminhos dos arquivos Excel
caminho_esm1 = r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM1_ESM.xlsx'
caminho_esm2 = r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM2_ESM.xlsx'
caminho_esm3 = r'C:\Users\USER\Desktop\dataser_PI-IV\12888_2022_4048_MOESM3_ESM.xlsx'

# Ler os arquivos e salvar em DataFrames
df_esm1 = pd.read_excel(caminho_esm1, header=0)
df_esm2 = pd.read_excel(caminho_esm2, header=0)
df_esm3 = pd.read_excel(caminho_esm3, header=1)

#Correção de linhas extras
df_esm1 = df_esm1.iloc[:-1, :]
df_esm2 = df_esm2.iloc[:-1, :]

# Mostrar as 5 primeiras linhas de cada para conferir
print("ESM1 - primeiras linhas:")
print(df_esm1.head())

print("\nESM2 - primeiras linhas:")
print(df_esm2.head())

print("\nESM3 - primeiras linhas:")
print(df_esm3.head())

# Função para explorar um DataFrame e mostrar informações importantes
def explorar_df(df, nome):
    print(f"\n📝 Explorando {nome}...\n")
    
    # Mostrar as 5 primeiras linhas para ter uma noção dos dados
    print("Primeiras 5 linhas:")
    print(df.head())
    
    # Mostrar as colunas disponíveis
    print("\nColunas disponíveis:")
    print(list(df.columns))
    
    # Mostrar o tipo de dado de cada coluna
    print("\nTipos de dados:")
    print(df.dtypes)
    
    # Verificar se tem dados faltantes (NaN) e quantos
    print("\nContagem de valores faltantes por coluna:")
    print(df.isna().sum())
    
    # Estatísticas descritivas para colunas numéricas
    print("\nEstatísticas descritivas para colunas numéricas:")
    print(df.describe())
    
    print("-"*50)

# Explorar cada DataFrame
explorar_df(df_esm1, "ESM1")
explorar_df(df_esm2, "ESM2")
explorar_df(df_esm3, "ESM3")
