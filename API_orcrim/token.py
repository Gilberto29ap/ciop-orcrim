import requests
from requests.auth import HTTPBasicAuth
import jwt
import time
from urllib.parse import urlencode
from config.settings import client_id
from config.settings import client_secret



token_url = "https://hmlsegurancaorcrim.mj.gov.br/auth/realms/hmlorcrim/protocol/openid-connect/token"



def get_token(token_url=token_url, client_id=client_id, client_secret=client_secret):
  # Parâmetros do corpo da requisição
  data = {
      'grant_type': 'client_credentials',
      'scope': 'openid profile orcrim-backend'  # Substitua pelos escopos necessários
  }

  # Realizando a requisição POST
  response = requests.post(token_url, auth=HTTPBasicAuth(client_id, client_secret), data=data)

  # Verificando a resposta
  if response.ok:
      # O token de acesso está na resposta
      token = response.json()['access_token']
      print("Token de Acesso:", token)
      return token
  else:
      print("Falha na obtenção do token:", response.text)
      return ""
  


def check_token(token):
    try:
        # Decodifica o token. Isso não verifica a assinatura, apenas decodifica o payload
        decoded_token = jwt.decode(token, options={"verify_signature": False})

        # Verifica se o token expirou
        exp_time = decoded_token.get('exp')
        if exp_time and exp_time > time.time():
            print("O token ainda é válido.")
            return True
        else:
            print("O token expirou.")
            return False
    except jwt.DecodeError:
        print("Erro ao decodificar o token. O token pode estar malformado.")
        return False
    except jwt.ExpiredSignatureError:
        print("O token expirou.")
        return False
    except Exception as e:
        print(f"Erro ao decodificar o token: {str(e)}")
        return False