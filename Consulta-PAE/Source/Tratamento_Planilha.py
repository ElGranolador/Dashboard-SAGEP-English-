import pandas as pd

def processar_planilha(input_file, output_file):
    try:
        # Carregue o arquivo XLSX em um DataFrame do Pandas
        df = pd.read_excel(input_file)

        # Exclua a primeira e a segunda coluna
        df = df.drop(columns=[df.columns[0], df.columns[1], df.columns[12]])

        # Renomeie as colunas
        df.columns = ['Protocolo', 'Data Entrada', 'Origem', 'Espécie', 'Assunto', 'Sub-Assunto', 'Interessado', 'Responsável', 'Pasta', 'Pendencias']

        # Exclua as linhas com números inteiros nas colunas especificadas
        columns_to_check = ['Protocolo', 'Data Entrada', 'Origem', 'Espécie', 'Assunto']

        for col in columns_to_check:
            df = df[~pd.to_numeric(df[col], errors='coerce').notna()]

        # Salve o DataFrame de volta em um novo arquivo XLSX ou sobrescreva o original
        df.to_excel(output_file, index=False)
        print("Processamento concluído com sucesso!")

    except Exception as e:
        print(f"Erro ao processar a planilha: {str(e)}")

# Exemplo de uso da função
#input_file = '/content/Planilha.xlsx'
#output_file = 'planilha_modificada.xlsx'
#processar_planilha(input_file, output_file)
