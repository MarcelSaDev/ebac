import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Configurar o estilo do Seaborn (opcional)
sns.set(style="whitegrid")

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df)

# Adicionar títulos e rótulos
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Rotacionar rótulos do eixo x para melhor visualização
plt.xticks(ticks=df.index, labels=['Dia {}'.format(i + 1) for i in range(len(df))])

# Salvar o gráfico como um arquivo PNG
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()
