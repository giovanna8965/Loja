def clean_data(df):
    """
    Limpa e prepara os dados para análise.

    Args:
        df (dask.dataframe.DataFrame): DataFrame original.

    Returns:
        dask.dataframe.DataFrame: DataFrame limpo.
    """
    # Verificar valores ausentes e removê-los
    df = df.dropna()
    
    # Remover duplicatas
    df = df.drop_duplicates()
    
    # Converter colunas de datas para o formato datetime
    df['data_venda'] = dd.to_datetime(df['data_venda'])
    
    return df
