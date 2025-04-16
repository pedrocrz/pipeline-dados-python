import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('relatorios/total_por_produto.csv')

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['produto'], df['total_vendido'], color='skyblue')
plt.title('Total Vendido por Produto')
plt.xlabel('Produto')
plt.ylabel('Total Vendido (R$) ')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvando a imagem
plt.savefig('relatorios/grafico_total_por_produto.png')
plt.show()
