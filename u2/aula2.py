# : DataFrame, NumPy e Quartis

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

Seleção de Dados: Loc, Iloc e Query
Aprender a selecionar dados de forma precisa é crucial:
● .loc: Para selecionar dados usando rótulos (nomes de colunas ou índices)
● .iloc: Para selecionar dados usando a posição numérica
● .query: Para filtrar dados com expressões mais complexas