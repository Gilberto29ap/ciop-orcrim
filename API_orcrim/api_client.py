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
            response: objeto resposta da requisição, possui métodos para serem manipulados
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

        """
        Envia uma requisição GET para obter informações de um uuid.

        Parâmetros:
            uuid (str): Uma string com o valor do uuid a ser consultado.

        Retorna:
            response: objeto resposta da requisição, possui métodos para serem manipulados
        """

        logging.info(f"Iniciando requisição GET de personalidade, uuid: {uuid}")

        url = f"{self.base_url}/api/v1/personalidade/{uuid}"
        token_de_autorizacao = TokenManager().get_access_token()

        headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token_de_autorizacao}'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Isso vai levantar uma exceção para respostas 4xx/5xx
            logging.info("Personalidade incluída com sucesso.")
            return response  # Retorna a resposta JSON da API
        except requests.HTTPError as http_err:
            logging.error(f"Erro HTTP ao fazer a requisição POST: {http_err}")
        except Exception as e:
            logging.error(f"Erro ao fazer a requisição POST: {e}")
        return response
    

    def post_telefone(self, uuid=None, telefone=None):

        """
        Envia uma requisição POST para inserir um novo telefone ao uuid.

        Parâmetros:
            uuid (str): Uma string com o UUID da personalidade.
            telefone (str, int): Uma string ou Inteiro com o número de telefone a ser inserido

        Retorna:
            response: objeto resposta da requisição, possui métodos para serem manipulados
        """
        

        url = f"{self.base_url}/api/v1/personalidade/{uuid}/telefones"
        token_de_autorizacao = TokenManager().get_access_token()

        dados_json = {"data": [{"telefone": f"{telefone}"}]}

        headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token_de_autorizacao}',
        'Content-Type': 'application/json'
        }

        logging.info(f"Iniciando POST de telefone para {uuid}")

        try:
            response = requests.post(url, headers=headers, json=dados_json)
            response.raise_for_status()  # Isso vai levantar uma exceção para respostas 4xx/5xx
            logging.info("Telefone incluído com sucesso.")
            return response  # Retorna a resposta JSON da API
        except requests.HTTPError as http_err:
            logging.error(f"Erro HTTP ao fazer a requisição POST: {http_err}")
        except Exception as e:
            logging.error(f"Erro ao fazer a requisição POST: {e}")
        return response
    

    def post_alcunhas(self, uuid=None, alcunha=None, data_alcunha=None):

        """
        Envia uma requisição POST para inserir uma nova alcunha ao uuid.

        Parâmetros:
            uuid (str): Uma string com o UUID da personalidade.
            telefone (str): Uma string com a alcunha a ser inserida

        Retorna:
            response: objeto resposta da requisição, possui métodos para serem manipulados
        """
        

        url = f"{self.base_url}/api/v1/personalidade/{uuid}/alcunhas"
        token_de_autorizacao = TokenManager().get_access_token()

        dados_json = {"data": [{"alcunha": f"{alcunha}"}, {"dataAlcunha": ""}]}

        headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token_de_autorizacao}',
        'Content-Type': 'application/json'
        }

        logging.info(f"Iniciando POST de alcunha para {uuid}")

        try:
            response = requests.post(url, headers=headers, json=dados_json)
            response.raise_for_status()  # Isso vai levantar uma exceção para respostas 4xx/5xx
            logging.info("Alcunha incluída com sucesso.")
            return response  # Retorna a resposta JSON da API
        except requests.HTTPError as http_err:
            logging.error(f"Erro HTTP ao fazer a requisição POST: {http_err}")
        except Exception as e:
            logging.error(f"Erro ao fazer a requisição POST: {e}")
        return response

