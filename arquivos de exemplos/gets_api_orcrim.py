import requests
import json

def busca_data_atualizacao(uuid):
    with open('./json/personalidade.json', 'r') as arquivo:
        dados = json.load(arquivo)
        lista = dados['data']
        for item in lista:
            if item['uuid'] == uuid:
                return item['dataAtualizacao']

def autenticar_usuario(url_autenticacao, user, password):
    data_payload = {
        "grant_type": 'client_credentials',
        "client_id": user,
        "client_secret": password,
        "scope": 'openid email profile orcrim-backend'
    }

    try:
        response = requests.post(url_autenticacao, data=data_payload)

        if response.status_code == 200:
            token = response.json()["access_token"]
            return token
        else:
            print(f"Erro na autenticação do Else: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na autenticação da Except: {e}")
        return None


def busca_gets_sem_param(token, base_url, endpoint):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(base_url + endpoint, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print(f"Erro na requisição else: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


def busca_gets_param(token, base_url, endpoint, param):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(base_url + endpoint, params=param, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print(f"Erro na requisição: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


# Função para ler arquivo JSON com UUID e retornar uma lista com UUIDs
def gera_lista_uuid_orcrim(arquivo):
    with open(arquivo, "r") as f:
        dados = json.load(f)

        lista = dados['data']

        lista_uuid = []

        for item_lista in lista:
            lista_uuid.append(item_lista["uuid"])

    return lista_uuid


def gera_json_faccionados_orcrim(token, base_url, endpoint):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(base_url + endpoint, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print(f"Erro na requisição: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
