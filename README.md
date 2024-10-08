# Projeto de Big Data com Pandas e Streamlit

Este projeto utiliza Pandas para manipulação e análise de dados e Streamlit para criação de dashboards interativos. Ele foi desenvolvido para uma empresa de tênis, com o objetivo de analisar dados de vendas, clientes e marketing, além de criar previsões de vendas.

## Pré-requisitos

Certifique-se de ter o Python 3.7+ instalado em sua máquina. Recomendamos o uso de um ambiente virtual para evitar conflitos de dependências.

## Configuração do Ambiente

### 1. Criar um Ambiente Virtual

Crie um ambiente virtual para o projeto usando o código:

 python -m venv myenv


2. Instalar Dependências
Instale as bibliotecas necessárias usando o pip:

pip install pandas matplotlib seaborn streamlit scikit-learn

Executando o Dashboard

1. Escrever o Código do Dashboard
Crie um arquivo chamado dashboard.py no diretório do projeto e adicione o seguinte código:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Carregar dados (Substitua os caminhos pelos seus arquivos de dados)
vendas = pd.read_csv('vendas.csv')
clientes = pd.read_csv('clientes.csv')
marketing = pd.read_csv('marketing.csv')


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


2. Executar o Dashboard
   
Para executar o dashboard, utilize o seguinte comando no terminal:

streamlit run dashboard.py

Isso abrirá uma nova janela no navegador exibindo o dashboard interativo.

Funcionalidades do Dashboard

Vendas por Categoria de Produto: Gráfico de barras mostrando a quantidade de vendas por categoria de produto.
Vendas ao Longo do Tempo: Gráfico de linha mostrando a quantidade de vendas ao longo do tempo (por mês).
Estatísticas Descritivas: Exibe estatísticas descritivas dos dados de vendas, clientes e marketing.
Previsão de Vendas: Gráfico de linha comparando os dados reais de vendas com as previsões feitas por um modelo de regressão linear simples.

