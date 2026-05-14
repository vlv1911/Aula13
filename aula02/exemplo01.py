import pandas as pd

df_eletronicos = pd.read_excel('vendas_eletronicos.xlsx')

# primeiras linhas
print(df_eletronicos.head(5))

print('\nMaior valor do faturamento')
print(45 * '=')
print(df_eletronicos['Faturamento Total (R$)'].max())

print('\nMenor valor do faturamento')
print(45 * '=')
print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax(), 'Produto'])
print(df_eletronicos['Faturamento Total (R$)'].min())

print('\nTotal de unidades vendidas')
print(45 * '=')
print(df_eletronicos['Unidades Vendidas'].sum())

print('\nPreço médio dos produtos')
print(45 * '=')
print(round(df_eletronicos['Preço por Unidade (R$)'].mean()))

print('\nProdutos acima da média')
print(45 * '=')
media = df_eletronicos['Faturamento Total (R$)'].mean()
print(df_eletronicos[df_eletronicos['Faturamento Total (R$)'] >= media])


# pip install openpyxl (plugin para ler planilhas do excel)

print(df_eletronicos.loc[df_eletronicos['Faturamento Total (R$)'].idxmax()])