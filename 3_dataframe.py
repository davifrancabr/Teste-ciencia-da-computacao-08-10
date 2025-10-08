import pandas as pd

pessoas = pd.read_csv('./data/pessoas.csv')
gostos = pd.read_csv('./data/gostos.csv')


def adicionar_gosto(pessoas_df: pd.DataFrame, gostos_df: pd.DataFrame):
    pessoas_lista = pessoas_df.to_dict('records')
    gostos_lista = gostos_df.to_dict('records')

    for pessoa in pessoas_lista:
        for gosto in gostos_lista:
            if pessoa['id'] == gosto['id']:
                pessoa['gostos'] = gosto['gostos']
    return pessoas_lista


resultado = adicionar_gosto(pessoas, gostos)


def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.DataFrame(pessoas)
    return df.to_csv(nome_arquivo, index=False)


exportar_csv(resultado, './data.csv')
