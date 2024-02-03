
from config.settings import client_id, client_secret, token_url, scopes
import requests
import time
import logging

# Configuração básica de logging
# logging.basicConfig(level=logging.INFO)

logging.basicConfig(level=logging.INFO,
                    filename='app.log',  # Nome do arquivo de log
                    filemode='a',  # Modo 'a' append adiciona ao arquivo existente
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TokenManager:
    """
    Gerencia a obtenção e renovação de tokens de acesso OAuth 2.0 com credenciais do cliente.

    Esta classe fornece uma maneira automatizada de solicitar e renovar tokens de acesso
    necessários para autenticar chamadas de API. Os tokens são renovados automaticamente
    quando expiram.

    Atributos:
        client_id (str): O ID do cliente obtido no registro do aplicativo OAuth.
        client_secret (str): O segredo do cliente associado ao ID do cliente.
        token_url (str): A URL completa para solicitar tokens de acesso.
        scopes (str): Uma string de escopos solicitados separados por espaços.

    Métodos:
        get_new_access_token(): Solicita um novo token de acesso usando as credenciais do cliente.
        get_access_token(): Retorna um token de acesso válido, solicitando um novo se necessário.
    """

    def __init__(self, client_id=client_id, client_secret=client_secret, token_url=token_url, scopes=scopes):
        """
        Inicializa uma nova instância do gerenciador de tokens com configurações específicas.

        Parâmetros:
            client_id (str): O ID do cliente para autenticação OAuth.
            client_secret (str): O segredo do cliente para autenticação OAuth.
            token_url (str): URL para solicitação do token de acesso.
            scopes (str): Escopos de acesso solicitados, separados por espaços.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.scopes = scopes
        self.token_data = {'access_token': None, 'expires_at': 0}

    def get_new_access_token(self):
        """
        Solicita um novo token de acesso ao servidor de autenticação.

        Usa as credenciais do cliente (client_id e client_secret) e os escopos definidos
        para solicitar um novo token de acesso. Armazena o novo token e sua data de expiração.

        Retorna:
            str: O token de acesso obtido.

        Levanta:
            Exception: Se a solicitação para obter um novo token de acesso falhar.
        """
        params = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': self.scopes
        }
        try:
            response = requests.post(self.token_url, data=params)
            response.raise_for_status()  # Lança uma exceção para respostas de erro HTTP
            token_info = response.json()
            self.token_data['access_token'] = token_info['access_token']
            self.token_data['expires_at'] = time.time() + token_info['expires_in'] - 30
            logging.info("Token de acesso atualizado com sucesso.")
            return token_info['access_token']
        except requests.RequestException as e:
            logging.error(f"Erro ao solicitar token de acesso: {e}")
            raise

    def get_access_token(self):
        """
        Obtém um token de acesso válido, solicitando um novo se o atual expirou.

        Verifica se o token de acesso atual ainda é válido (não expirou) e, se expirou,
        solicita um novo. Isso garante que sempre um token válido seja retornado para uso.

        Retorna:
            str: Um token de acesso válido.
        """
        if self.token_data['access_token'] is None or time.time() > self.token_data['expires_at']:
            logging.info("Token de acesso expirado ou ausente. Solicitando um novo.")
            return self.get_new_access_token()
        else:
            return self.token_data['access_token']

