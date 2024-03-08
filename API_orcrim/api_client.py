import requests
import logging
from config.settings import API_BASE_URL
from API_orcrim.token import TokenManager

# Configuração básica do logging
logging.basicConfig(level=logging.INFO,
                    filename='app.log',  # Nome do arquivo de log
                    filemode='a',  # Modo 'a' append adiciona ao arquivo existente
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ApiClient:
    def __init__(self):
        """
        Inicializa o cliente da API usando a URL base definida no arquivo de configuração.
        """
        self.base_url = API_BASE_URL
        self.token = None

    def post_personalidade(self, personalidade_data):
        """
        Envia uma requisição POST para criar uma nova personalidade no sistema.

        Parâmetros:
            personalidade_data (dict): Um dicionário contendo os dados da personalidade.

        Retorna:
            dict or None: A resposta da requisição convertida de JSON para um dicionário,
            ou None em caso de falha.
        """

        url = f"{self.base_url}/api/v1/personalidade"
        token_de_autorizacao = TokenManager().get_access_token()
        dados_json = personalidade_data
        headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token_de_autorizacao}',
        'Content-Type': 'application/json'
        }

        logging.info(f"Iniciando requisição POST para {url}")

        try:
            response = requests.post(url, headers=headers, json=dados_json)
            response.raise_for_status()  # Isso vai levantar uma exceção para respostas 4xx/5xx
            logging.info("Personalidade incluída com sucesso.")
            return response  # Retorna a resposta JSON da API
        except requests.HTTPError as http_err:
            logging.error(f"Erro HTTP ao fazer a requisição POST: {http_err}")
        except Exception as e:
            logging.error(f"Erro ao fazer a requisição POST: {e}")
        return response


    def get_personalidade(self, uuid=None):

        logging.info(f"Iniciando requisição GET de personalidade, uuid: {uuid}")

        url = f"{self.base_url}/api/v1/personalidade/{uuid}"
        token_de_autorizacao = TokenManager().get_access_token()

        headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token_de_autorizacao}'
        }

        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()  # Isso vai levantar uma exceção para respostas 4xx/5xx
            logging.info("Personalidade incluída com sucesso.")
            return response  # Retorna a resposta JSON da API
        except requests.HTTPError as http_err:
            logging.error(f"Erro HTTP ao fazer a requisição POST: {http_err}")
        except Exception as e:
            logging.error(f"Erro ao fazer a requisição POST: {e}")
        return response
