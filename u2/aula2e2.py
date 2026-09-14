import pandas as pd
# Carregar a planilha 'Transacoes' para um DataFrame
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
# Exibir as primeiras 5 linhas para verificar os dados
print(df_transacoes.head())