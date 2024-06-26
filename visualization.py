import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(vendas_mensais, vendas_produto):
    """
    Cria visualizações dos dados analisados.

    Args:
        vendas_mensais (pandas.DataFrame): Dados de vendas mensais.
        vendas_produto (pandas.DataFrame): Dados de vendas por produto.
    """
    # Converter os dados para pandas DataFrame para visualização
    vendas_mensais_pd = vendas_mensais.reset_index()
    vendas_produto_pd = vendas_produto.reset_index()
    
    # Visualização de Vendas Mensais
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=vendas_mensais_pd, x='mes', y='receita', hue='ano')
    plt.title('Vendas Mensais ao Longo dos Anos')
    plt.xlabel('Mês')
    plt.ylabel('Receita')
    plt.show()
    
    # Visualização de Vendas por Produto
    plt.figure(figsize=(12, 6))
    sns.barplot(data=vendas_produto_pd, x='produto', y='receita')
    plt.title('Receita por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Receita')
    plt.xticks(rotation=45)
    plt.show()
