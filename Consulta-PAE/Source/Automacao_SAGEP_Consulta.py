from playwright.sync_api import sync_playwright
import time
import pandas as pd
import playwright
from playwright.sync_api import Page, ElementHandle
from playwright.sync_api import TimeoutError

# import Tratamento_Planilha as tp


# Criar DataFrame
df_global = pd.DataFrame()

def run_automation():
    global df_global  # Indica que estamos referenciando a variável global, não local
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        page = context.new_page()
        page.goto('https://www.sistemas.pa.gov.br/governodigital/public/main/index.xhtml')
        
        # Preenchendo o campo "Usuário" e "Senha" (nota: você precisará identificar corretamente os seletores destes campos)
        page.fill('#form_login\\:login_username', 'seu.login')
        page.fill('#form_login\\:login_password', 'SuaSenha')
        
        page.click('#form_login\\:button_login')
        
        page.wait_for_selector('#form_sistema\\:submit_area > div > div:nth-child(2) > div.SistemaGridLabel > a > p')

        page.click('#form_sistema\\:submit_area > div > div:nth-child(2) > div.SistemaGridLabel > a > p')

        time.sleep(3)
       
        new_page = page.wait_for_event('popup')
        
        new_page.click('#iconmenu_vert\\:panelMenuGroupConsulta')
        
        new_page.wait_for_selector('#iconmenu_vert\\:j_id95')

        new_page.click('#iconmenu_vert\\:j_id95')

        new_page.wait_for_selector('#iconmenu_vert\\:j_id103')

        new_page.click('#iconmenu_vert\\:j_id103')

        new_page.wait_for_selector('#protocolo_form_pesq\\:protocolo')

        df = pd.read_excel('Planilha_Protocolos\AGA01.xlsx')

        time.sleep(2)

        
        for protocolo in df.iloc[:, 0]:
            new_page.fill('#protocolo_form_pesq\\:protocolo', protocolo)
            new_page.click('#protocolo_form_pesq\\:botaoPesquisar')
            time.sleep(2)
            
            df_extracao_protocolo = extract_table_data(new_page)

            # Adicionar coluna 'protocolo' ao df_extracao_protocolo
            df_extracao_protocolo['protocolo'] = protocolo
            
            # Incluir linhas do segundo DataFrame no primeiro usando pd.concat
            df_global = pd.concat([df_global, df_extracao_protocolo], ignore_index=True)

        df_global.to_excel('Planilha_Bruta\\Planilha_Bruta.xlsx', index=False)

        #breakpoint()

        browser.close()

'''

def extract_table_data(page):
    # Aguarde a tabela estar presente na página
    page.wait_for_selector('#protocolo_form_consulta\\:tramitacoes')

    # Extrair os dados da tabela 
    table_rows = page.locator('#protocolo_form_consulta\\:tramitacoes tbody tr').all()

    table_data = []
    for row in table_rows:
        columns = row.locator('td').all()  
        row_data = [column.text_content() for column in columns]
        table_data.append(row_data)

    # Convertendo os dados para um DataFrame
    df = pd.DataFrame(table_data)

    return df

'''

def extract_table_data(page):
    try:
        # Aguarde a tabela estar presente na página
        page.wait_for_selector('#protocolo_form_consulta\\:tramitacoes')

        # Extrair os dados da tabela 
        table_rows = page.locator('#protocolo_form_consulta\\:tramitacoes tbody tr').all()

        table_data = []
        for row in table_rows:
            columns = row.locator('td').all()  
            row_data = [column.text_content() for column in columns]
            table_data.append(row_data)

        # Convertendo os dados para um DataFrame
        df = pd.DataFrame(table_data)

        return df
    except TimeoutError:
        print("Timeout excedido ao esperar pelo seletor. Retornando DataFrame vazio.")
        return pd.DataFrame()



if __name__ == '__main__':
    run_automation()

    
