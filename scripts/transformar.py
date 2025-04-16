def transformar_dados(df):
    df = df.dropna(subset=['preco', 'quantidade']) # Para remover linhas incompletas
    df['preço'] = df['preco'].astype(float)
    df['quantidade'] = df['quantidade'].astype(int)
    df['total'] = df['preco'] * df['quantidade']
    return df

