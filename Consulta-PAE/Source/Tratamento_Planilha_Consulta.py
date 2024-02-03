import pandas as pd

def processar_planilha(caminho_do_arquivo, nome_do_arquivo_saida):
    # Carregando a planilha Excel em um DataFrame
    df = pd.read_excel(caminho_do_arquivo)
    
    # Renomeando as colunas
    df.columns = ['Número', 'Origem', 'Data Envio', 'Usuário que tramitou', 'Destino', 'Data recebimento', 'Usuário que recebeu', 'Estafeta', 'Protocolo']

    # Movendo a última coluna para a primeira posição
    df = df[['Protocolo'] + [col for col in df.columns if col != 'Protocolo']]

    # Ordenando a tabela por Data Envio (descomente a linha abaixo se quiser ordenar)
    # df = df.sort_values(by='Data Envio')

    #df = df.drop_duplicates()

    # Exportando o DataFrame para uma planilha Excel
    df.to_excel(nome_do_arquivo_saida, index=False)

# Substitua 'caminho/do/arquivo/seu_arquivo.xlsx' pelo caminho real do seu arquivo
caminho_do_arquivo_entrada = 'Planilha_Bruta\\Planilha_Judiciais_bruta_consulta.xlsx'

# Substitua 'nome_do_arquivo.xlsx' pelo nome desejado para o arquivo de saída
nome_do_arquivo_saida = 'Planilha_Pronta\\Planilha_Judiciais_Pronta.xlsx'

# Chamando a função com os parâmetros adequados
processar_planilha(caminho_do_arquivo_entrada, nome_do_arquivo_saida)
