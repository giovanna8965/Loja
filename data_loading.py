import dask.dataframe as dd

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV usando Dask.

    Args:
        file_path (str): Caminho para o arquivo CSV.

    Returns:
        dask.dataframe.DataFrame: DataFrame carregado.
    """
    df = dd.read_csv(file_path)
    return df
