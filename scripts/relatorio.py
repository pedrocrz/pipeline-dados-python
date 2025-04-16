import sqlite3
import pandas as pd

# Relatório total vendido por produto
def total_por_produto(caminho_db):
    con = sqlite3.connect(caminho_db)
    consulta = """
            SELECT produto, SUM(total) as total_vendido
            FROM vendas
            GROUP BY produto
            ORDER BY total_vendido DESC        
            """
    df_relatorio = pd.read_sql_query(consulta, con)
    df_relatorio.to_csv('relatorios/total_por_produto.csv', index=False)
    con.close()
    print('Relatório total por produto gerado com sucesso!')
    
# Relatório de vendas por dia
def vendas_por_dia(caminho_db):
    con = sqlite3.connect(caminho_db)
    consulta = """
                SELECT data, SUM(total) as total_diario
                FROM vendas
                GROUP BY data
                ORDER BY data
                """
    df_dia = pd.read_sql_query(consulta, con)
    df_dia.to_csv('relatorios/vendas_por_dia.csv', index=False)
    con.close()
    print('Relatório de vendas por dia gerado com sucesso!')

# Relatório de produto mais vendido(quantidade)
def quantidade_vendida(caminho_db):
    con = sqlite3.connect(caminho_db)
    consulta = """
                SELECT produto, SUM(quantidade) as total_vendido
                FROM vendas
                GROUP BY produto
                ORDER BY total_vendido DESC
                """
    df_quantidade = pd.read_sql_query(consulta, con)
    df_quantidade.to_csv('relatorios/quantidade_por_produto.csv', index=False)
    con.close()
    print('Relatório de quantidade vendida por produto gerado com sucesso!')
    