import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configurar estilo de visualização do Seaborn
sns.set(style="whitegrid")

# Carregar dados (Substitua os caminhos pelos seus arquivos de dados)
vendas = pd.read_csv('vendas.csv')
clientes = pd.read_csv('clientes.csv')
marketing = pd.read_csv('marketing.csv')

# Tratar dados (conversão de data e remoção de nulos)
vendas['data_venda'] = pd.to_datetime(vendas['data_venda'])
vendas.dropna(inplace=True)
clientes.dropna(inplace=True)
marketing.dropna(inplace=True)

# Análises
vendas_por_categoria = vendas.groupby('categoria')['quantidade'].sum().reset_index()
vendas['mes'] = vendas['data_venda'].dt.to_period('M')
vendas_por_mes = vendas.groupby('mes')['quantidade'].sum().reset_index()

# Título do Dashboard
st.title('Dashboard de Vendas da Empresa de Tênis')

# Seção 1: Vendas por Categoria
st.header('Vendas por Categoria de Produto')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='categoria', y='quantidade', data=vendas_por_categoria, ax=ax1)
ax1.set_title('Vendas por Categoria de Produto')
ax1.set_xlabel('Categoria')
ax1.set_ylabel('Quantidade Vendida')
st.pyplot(fig1)

# Seção 2: Vendas ao Longo do Tempo
st.header('Vendas ao Longo do Tempo')
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(x='mes', y='quantidade', data=vendas_por_mes, ax=ax2)
ax2.set_title('Vendas ao Longo do Tempo')
ax2.set_xlabel('Mês')
ax2.set_ylabel('Quantidade Vendida')
st.pyplot(fig2)

# Análise descritiva
st.header('Estatísticas Descritivas')
st.subheader('Vendas')
st.write(vendas.describe())
st.subheader('Clientes')
st.write(clientes.describe())
st.subheader('Marketing')
st.write(marketing.describe())

# Modelo preditivo (Simples para ilustração)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Preparar dados para previsão
X = vendas_por_mes['mes'].apply(lambda x: x.ordinal).values.reshape(-1, 1)
y = vendas_por_mes['quantidade'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prever no conjunto de teste
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

st.header('Previsão de Vendas')
st.write(f'Erro Quadrático Médio: {mse}')
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.lineplot(x=X_test.flatten(), y=y_test, label='Dados Reais', ax=ax3)
sns.lineplot(x=X_test.flatten(), y=y_pred, label='Previsão', ax=ax3)
ax3.set_title('Previsão de Vendas')
ax3.set_xlabel('Mês')
ax3.set_ylabel('Quantidade Vendida')
st.pyplot(fig3)
