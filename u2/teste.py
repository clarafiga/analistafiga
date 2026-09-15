import pandas as pd
import numpy as np
import matplotlib.pyplot as py

# Dados de exemplo
dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

# Calcular quartis
q1 = np.percentile(dados, 25) # O 1º quartil representa 25% dos dados
q2 = np.percentile(dados, 50) # A Mediana é o mesmo que o quartil de 50%
q3 = np.percentile(dados, 75) # O 3º quartil representa 75% dos dados

# Exibir os resultados
print(f"Primeiro quartil (Q1): {q1}")
print(f"Segundo quartil (Q2, Mediana): {q2}")
print(f"Terceiro quartil (Q3): {q3}")

# Calcule o Q1, Q2 (Mediana) e Q3 para a coluna 'preco'
q1_preco = df_transacoes['preco'].quantile(0.25)
q2_preco = df_transacoes['preco'].quantile(0.50)
q3_preco = df_transacoes['preco'].quantile(0.75)
print(f"Preço Q1: {q1_preco}")
print(f"Preço Mediana (Q2): {q2_preco}")
print(f"Preço Q3: {q3_preco}")
