def analyze_data(df):
    """
    Realiza a análise exploratória dos dados.

    Args:
        df (dask.dataframe.DataFrame): DataFrame limpo.

    Returns:
        tuple: Dados de vendas mensais e por produto.
    """
    # Adicionar colunas de ano e mês
    df['ano'] = df['data_venda'].dt.year
    df['mes'] = df['data_venda'].dt.month
    
    # Agrupar dados por ano e mês
    vendas_mensais = df.groupby(['ano', 'mes'])['receita'].sum().compute()
    
    # Agrupar dados por produto
    vendas_produto = df.groupby('produto')['receita'].sum().compute()
    
    return vendas_mensais, vendas_produto
