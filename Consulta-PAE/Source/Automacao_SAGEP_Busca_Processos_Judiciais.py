from playwright.sync_api import sync_playwright
import time
import pandas as pd
import playwright
from playwright.sync_api import Page, ElementHandle

import Tratamento_Planilha as tp

def run_automation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
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
        
        new_page.click('#iconmenu_vert\\:panelMenuGroupProtocoloEletronico')
        
        new_page.wait_for_selector('#iconmenu_vert\\:j_id52')

        new_page.click('#iconmenu_vert\\:j_id52')

        new_page.wait_for_selector('#iconmenu_vert\\:panelMenuItemEscaninhoUnidade')

        new_page.click('#iconmenu_vert\\:panelMenuItemEscaninhoUnidade')

        select_field_selector = '#escaninho_consult_pesq\\:unidade'
        option_value = 'SAGEP - SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS - SE01'

        #Seletor Processo Judicial
        select_field_selector = '#escaninho_consult_pesq\\:selectOneMenuPastas'
        option_value = 'PROCESSO JUDICIAL'

        new_page.select_option(select_field_selector, value=option_value)

        new_page.click('#escaninho_consult_pesq\\:botaoPesquisar')

        df = extract_and_store_table_data(new_page)

        df = df.drop_duplicates(keep='first')
        
        df.to_excel("Planilha_Não_Tratada\\Planilha_Judicial.xlsx", index=False)


        tp.processar_planilha('Planilha_Não_Tratada\\Planilha_Judicial.xlsx', 'Planilha_Tratada\\Planilha_Processos_Judicial.xlsx')

        browser.close()


def extract_and_store_table_data(page):
    all_data = None  # Inicialize com None para verificar a primeira iteração
    previous_data = None
    consecutive_same_data_count = 0  # Contador de páginas consecutivas com os mesmos dados

    while True:
        try:
            # Aguarde a tabela estar presente na página
            page.wait_for_selector('#escaninho_consult_pesq\\:table tbody tr')

            # Extrair os dados da tabela na página atual
            table_rows = page.locator('#escaninho_consult_pesq\\:table tbody tr').all()

            table_data = []
            for row in table_rows:
                columns = row.locator('td').all()
                row_data = [column.evaluate('(element) => element.textContent', timeout=10000) for column in columns]
                table_data.append(row_data)

            if table_data == previous_data:
                consecutive_same_data_count += 1
            else:
                consecutive_same_data_count = 0

            # Verifique se a próxima página é igual à anterior
            if consecutive_same_data_count >= 3:
                break

            previous_data = table_data

            if all_data is None:
                all_data = table_data
            else:
                all_data.extend(table_data)

            # Verificar se há próxima página e navegar, se disponível
            next_page_button = page.locator('#escaninho_consult_pesq\\:table\\:paginador_table > tbody > tr > td:nth-child(8)')
            if not next_page_button.is_disabled():
                next_page_button.click()
                # Aguarde um tempo para o carregamento da próxima página
                page.wait_for_timeout(2000)  # Ajuste o tempo de espera conforme necessário
            else:
                break
        except Exception as e:
            print(f"Erro: {e}")
            break
            time.sleep(1)

    # Convertendo os dados para um DataFrame
    df = pd.DataFrame(all_data)

    return df


if __name__ == '__main__':
    run_automation()
