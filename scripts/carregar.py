import sqlite3
 
def carregar_dados(df, caminho_db):
    try:
        conexao = sqlite3.connect(caminho_db)
        df.to_sql('vendas', conexao, if_exists='replace', index=False)
        conexao.close()
        print('Dados carregados com sucesso!')

    except Exception as e:
        print(f'Erro ao carregar dados: {e}')
        
