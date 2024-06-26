from data_loading import load_data
from data_cleaning import clean_data
from data_analysis import analyze_data
from visualization import visualize_data

def main():
    # Carregar os dados
    df = load_data('vendas.csv')
    
    # Limpar e preparar os dados
    df_clean = clean_data(df)
    
    # Analisar os dados
    vendas_mensais, vendas_produto = analyze_data(df_clean)
    
    # Visualizar os resultados
    visualize_data(vendas_mensais, vendas_produto)

if __name__ == "__main__":
    main()
