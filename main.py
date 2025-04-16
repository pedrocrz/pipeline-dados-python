from scripts.extrair import extrair_dados
from scripts.transformar import transformar_dados
from scripts.carregar import carregar_dados
from scripts.relatorio import (
    total_por_produto,
    vendas_por_dia,
    quantidade_vendida)

caminho_csv = '/home/pedro-cruz/Documentos/pipeline/dados/vendas.csv'
caminho_db = '/home/pedro-cruz/Documentos/pipeline/database/vendas.db'

df_bruto = extrair_dados(caminho_csv)
if df_bruto is not None:
    df_limpo = transformar_dados(df_bruto)
    carregar_dados(df_limpo, caminho_db)
    
    # Relatórios
    total_por_produto(caminho_db)
    vendas_por_dia(caminho_db)
    quantidade_vendida(caminho_db)


