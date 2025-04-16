import pandas as pd 

def extrair_dados(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv)
        return df
    except Exception as e:
        print(f'Erro ao extrair dados: {e}')
        return None
    