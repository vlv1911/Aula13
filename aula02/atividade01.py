import pandas as pd

vd_roupas = pd.read_excel('vendas_roupas.xlsx')

print(vd_roupas)

print('\nQuantidade total de peças vendidas:')
print(110 * '=')
print(vd_roupas['Unidades Vendidas'].sum())

print('\nMédia de preço dos produtos:')
print(110 * '=')
print(vd_roupas['Preço por Unidade (R$)'].mean())

print('\nProduto com maior faturamento:')
print(110 * '=')
print(vd_roupas['Faturamento Total (R$)'].max())

print('\nProduto com menor faturamento:')
print(110 * '=')
print(vd_roupas['Faturamento Total (R$)'].min())

print('\nProduto com nível de satisfação mais baixo:')
print(110 * '=')
print(vd_roupas[vd_roupas['Satisfação'] == 'Baixo'])

print('\nProduto com faturamento acima da média:')
print(110 * '=')
media = vd_roupas['Faturamento Total (R$)'].mean()
print(vd_roupas[vd_roupas['Faturamento Total (R$)'] >= media])



