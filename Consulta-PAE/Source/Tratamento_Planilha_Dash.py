import pandas as pd
import numpy as np
from datetime import datetime

def processar_dados_judiciais(caminho_arquivo):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

        # Defina as condições e os valores correspondentes
    conditions = [
        (df['Origem'] == 'SEDUC » Aposentadoria Novo » SE01'),
        (df['Origem'] == 'SEDUC » CADDEP - COORDENADORIA DE AVALIAÇÃO DE DESEMPENHO E DESENVOLVIMENTO PROFISSIONAL » SE01'),
        (df['Origem'] == 'SEDUC » CAPO/Abono - CAPO/Abono Permanência » SE01'),
        (df['Origem'] == 'SEDUC » CAPO/Abono Permanência » SE01'),
        (df['Origem'] == 'SEDUC » CAPO/AN - Aposentadoria Novo » SE01'),
        (df['Origem'] == 'SEDUC » CAPO/Judicial - CAPO Aposentadoria Judicial » SE01'),
        (df['Origem'] == 'SEDUC » CAPO/Triagem - Capo Triagem » SE01'),
        (df['Origem'] == 'SEDUC » CCM - COORDENADORIA DE CONTROLE E MOVIMENTAÇÃO » SE01'),
        (df['Origem'] == 'SEDUC » CCM Averbação » SE01'),
        (df['Origem'] == 'SEDUC » CCM Certidões » SE01'),
        (df['Origem'] == 'SEDUC » CCM DESIG/SUBS. - CCM Designação e Substituição » SE01'),
        (df['Origem'] == 'SEDUC » CCM Férias » SE01'),
        (df['Origem'] == 'SEDUC » CCM JUDICIAL PECUNIA » SE01'),
        (df['Origem'] == 'SEDUC » CCM Licença Especial » SE01'),
        (df['Origem'] == 'SEDUC » CCM- Pecúnia » SE01'),
        (df['Origem'] == 'SEDUC » CCM/Certidões - CCM Certidões » SE01'),
        (df['Origem'] == 'SEDUC » CCM/Férias - CCM Férias » SE01'),
        (df['Origem'] == 'SEDUC » CCM/Férias/Ass. - CCM FÉRIAS/ASSINATURA » SE01'),
        (df['Origem'] == 'SEDUC » CCM/JUD/Pecunia - CCM JUDICIAL PECUNIA » SE01'),
        (df['Origem'] == 'SEDUC » CCM/LicAssinar - CCM - Licenças Assinatura » SE01'),
        (df['Origem'] == 'SEDUC » CCM/LicESp - CCM Licença Especial » SE01'),
        (df['Origem'] == 'SEDUC » CCM/Pecúnia - CCM- Pecúnia » SE01'),
        (df['Origem'] == 'SEDUC » Cessão e Revogação Assinatura CCM » SE01'),
        (df['Origem'] == 'SEDUC » CFOP - COORDENADORIA DE FOLHA DE PAGAMENTO » SE01'),
        (df['Origem'] == 'SEDUC » COORDENADORIA DE CONTROLE E MOVIMENTAÇÃO » SE01'),
        (df['Origem'] == 'SEDUC » COORDENADORIA DE FOLHA DE PAGAMENTO » SE01'),
        (df['Origem'] == 'SEDUC » COORDENADORIA DE ORGANIZAÇÃO DE REDE » SE01'),
        (df['Origem'] == 'SEDUC » COORDENADORIA DE PLANEJAMENTO E SELEÇÃO » SE01'),
        (df['Origem'] == 'SEDUC » COORDENADORIA DE VALORIZAÇÃO E ASSISTÊNCIA AOS SERVIDORES » SE01'),
        (df['Origem'] == 'SEDUC » COR - COORDENADORIA DE ORGANIZAÇÃO DE REDE » SE01'),
        (df['Origem'] == 'SEDUC » COR/CODIGO - COR CODIGO » SE01'),
        (df['Origem'] == 'SEDUC » COR/RETROATIVO - COR Retroativo » SE01'),
        (df['Origem'] == 'SEDUC » CPS - COORDENADORIA DE PLANEJAMENTO E SELEÇÃO » SE01'),
        (df['Origem'] == 'SEDUC » CVAS - COORDENADORIA DE VALORIZAÇÃO E ASSISTÊNCIA AOS SERVIDORES » SE01'),
        (df['Origem'] == 'SEDUC » CVAS-Assist. - Coordenadoria de Assistência » SE01'),
        (df['Origem'] == 'SEDUC » CVAS-LA/Assina - CVAS Licença Aprimoramento Assinatura » SE01'),
        (df['Origem'] == 'SEDUC » DESIGASSINATURA - CCM Designação e Dispensa Assinatura » SE01'),
        (df['Origem'] == 'SEDUC » DIOP - DIRETORIA DE ORGANIZAÇÃO DE PESSOAL » SE01'),
        (df['Origem'] == 'SEDUC » DIRETORIA DE ORGANIZAÇÃO DE PESSOAL » SE01'),
        (df['Origem'] == 'SEDUC » SAGEP - SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS » SE01'),
        (df['Origem'] == 'SEDUC » SAGEP Cessão e Redistribuição » SE01'),
        (df['Origem'] == 'SEDUC » SAGEP Contrato Temporário PSS » SE01'),
        (df['Origem'] == 'SEDUC » SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS » SE01')
    ]

    values = [
        'DIOP CAPO', 'DIPSE CADDEP', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO',
        'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM',
        'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM',
        'DIOP CAPO', 'DIFOB CFOP', 'DIOP CCM', 'DIFOB CFOP',
        'DIOP COR', 'DIPSE CPS', 'DIFOB CVAS', 'DIOP COR', 'DIOP COR', 'DIOP COR',
        'DIPSE CPS', 'DIFOB CVAS', 'DIFOB CVAS', 'DIFOB CVAS', 'DIOP CCM',
        'DIOP Diretoria', 'DIOP', 'SAGEP Gabinete', 'SAGEP Gabinete', 'DIPSE CPS', 'SAGEP Gabinete'
    ]

    # Crie a nova coluna 'Setor Traduzido' com base nas condições e valores
    df['Setor Traduzido'] = np.select(conditions, values, default='')

    # Crie a coluna 'Pertence SAGEP' e defina os valores como 'Sim' onde as condições se aplicam
    df['Pertence SAGEP'] = np.where(df['Setor Traduzido'] != '', 'Sim', '')

    # Substitua todos os valores vazios na coluna 'Pertence SAGEP' por 'Não'
    df['Pertence SAGEP'].replace('', 'Não', inplace=True)

    # Substitua '%d/%m/%Y' pelo formato de data do seu arquivo Excel, se for diferente
    df['Data Envio'] = pd.to_datetime(df['Data Envio'], format='%d/%m/%Y')
    df['Data recebimento'] = pd.to_datetime(df['Data recebimento'], format='%d/%m/%Y')

    # Ordene o DataFrame pelo N° Protocolo e Data envio
    df.sort_values(by=['Protocolo', 'Data Envio'], inplace=True)

    # Redefina o índice do DataFrame
    df.reset_index(drop=True, inplace=True)

    # Crie uma nova coluna 'tempo de resposta' preenchida com valores vazios
    df['Tempo de resposta'] = None

    # Converta a coluna 'Data envio' para o tipo datetime, caso ainda não esteja
    df['Data Envio'] = pd.to_datetime(df['Data Envio'], format='%d/%m/%Y')

    # Calcule o tempo de resposta com base na próxima linha com o mesmo protocolo
    for index, row in df.iterrows():
        if index < len(df) - 1 and df.at[index, 'Protocolo'] == df.at[index + 1, 'Protocolo']:
            time_difference = df.at[index + 1, 'Data Envio'] - row['Data Envio']
            df.at[index, 'Tempo de resposta'] = time_difference.days

    # Passo 1: Identificar linhas com 'tempo de resposta' vazias
    linhas_com_tempo_vazio = df['Tempo de resposta'].isnull()

    # Passo 2: Calcular a data atual
    data_atual = datetime.now()

    # Passo 3: Calcular a diferença entre a data atual e 'Data envio' para as linhas identificadas
    df['Tempo parado'] = data_atual - df.loc[linhas_com_tempo_vazio, 'Data Envio']

    # Converter a diferença em dias para um número inteiro
    df['Tempo parado'] = (data_atual - df.loc[linhas_com_tempo_vazio, 'Data Envio']).dt.days

    # Aplicar a função abs() apenas aos valores não nulos na coluna "Tempo de resposta"
    df['Tempo de resposta'] = df['Tempo de resposta'].apply(lambda x: abs(x) if x is not None else None)

    # Filtrar o DataFrame para incluir apenas as linhas em que 'Pertence SAGEP' é igual a 'Sim'
    df_filtrado = df[df['Pertence SAGEP'] == 'Sim']

    # Carregando o dataframe original
    df_tempo = df_filtrado

    # Filtrando para remover valores nulos na coluna 'Tempo de resposta'
    df_tempo = df_tempo[df_tempo['Tempo de resposta'].notnull()]

    # Agrupando por 'Origem' e calculando a média de 'Tempo de resposta'
    df_resumo = df_tempo.groupby('Origem')['Tempo de resposta'].mean().reset_index()

    # Renomeando coluna
    df_resumo = df_resumo.rename(columns={'Tempo de resposta': 'Tempo médio de resposta'})

    # Crie o DataFrame df_criticos com os valores da coluna 'Tempo parado' maiores que 2
    df_criticos = df_filtrado[df_filtrado['Tempo parado'] > 2]

    # Salvando os DataFrames em novos arquivos Excel
    df.to_excel('Planilha_Dash\\Planilha_Judiciais_Pronta_Dash.xlsx', index=False)
    df_resumo.to_excel('Planilha_Dash\\Planilha_Judiciais_Pronta_Tempo_medio_Dash.xlsx', index=False)

# Para usar a função, você chama com o caminho do seu arquivo:
processar_dados_judiciais('Planilha_Pronta\\Planilha_Judiciais_Pronta.xlsx')
