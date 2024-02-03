# Automação com Playwright para SAGEP (SEDUC)

Este projeto foi desenvolvido com o objetivo de automatizar a coleta de números de protocolos do sistema da SEDUC referentes ao SAGEP, armazená-los e, posteriormente, inseri-los em um DataFrame para salvá-los em uma planilha.

## 📖 Dicionário de Dados

| Campo                | Descrição                                                            |
|----------------------|----------------------------------------------------------------------|
| `Protocolo`          | Número de protocolo referente a SAGEP                                |
| `Data Entrada`       | Data Entrada do Protocolo                      |
| `Origem`             | Setor de Origem do Protocolo                   |
| `Espécie`            | Tipo de protocolo                              |
| `Assunto`   | Assunto Principal do protocolo          |
| `SubAssunto`   | SubAssunto do Protocolo         |
| `numero_protocolo`   | Número de protocolo referente ao SAGEP         |
| `numero_protocolo`   | Número de protocolo referente ao SAGEP         |
| `numero_protocolo`   | Número de protocolo referente ao SAGEP         |
| `numero_protocolo`   | Número de protocolo referente ao SAGEP         |
| `numero_protocolo`   | Número de protocolo referente ao SAGEP         |

(Não se esqueça de adicionar todos os campos que serão usados no seu projeto.)

## 🛠️ Pré-requisitos

- Python (versão 3.12.0)
- [Playwright](https://playwright.dev/)
- Pandas
- Openpyxl

## 🚀 Guia de Instalação

1. **Clone o Repositório**

git clone https://endereco.do.seu.repositorio/projeto.git cd projeto


2. **Instale as Dependências**

Com o terminal aberto no diretório do projeto, execute:

pip install -r requirements.txt


3. **Configuração Adicional**

(Aqui você pode incluir qualquer configuração adicional necessária para o projeto. Por exemplo, definição de variáveis de ambiente, configurações específicas, etc.)

4. **Executando o Script**

Com tudo pronto, você pode iniciar o processo de automação com:

python nome_do_script.py

