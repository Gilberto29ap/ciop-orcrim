from gets_api_orcrim import autenticar_usuario, busca_gets_param
import datetime
import json


# client_id do usuário E client_secret do usuário
user_hml = ''
password_hml = ''

# url de autenticação: gera o token
url_autenticacao_hml = 'https://hmlsegurancaorcrim.mj.gov.br/auth/realms/hmlorcrim/protocol/openid-connect/token'

# Geração do token
token = autenticar_usuario(url_autenticacao_hml, user_hml, password_hml)

# url do ambiente da base de dados
base_url = "https://hmlorcrim.mj.gov.br/backend-orcrim/api/v1"

endpoint = '/personalidade'

# Cria o param data início e data fim para busca dos UUIDs do período
data_hora_atual = datetime.datetime.now()
formato = "%d/%m/%Y %H:%M:%S.%f"

data_ini = '01/01/2010 00:00:00.000'  # Data Inicial
data_fim = str(data_hora_atual.strftime(formato)[:-3])  # Data Final

param = {
    'dataInicio': data_ini,
    'dataFim': data_fim
}

if token:  # Autenticação OK
    nome_arquivo = './json' + endpoint + '.json'  # Gera o Arquivo de saída personalidade.json
    # Busca os UUIDs atualizados de acordo com o perído informado
    dados = busca_gets_param(token, base_url, endpoint, param)

    if dados:  # Se possui dados
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo)

        print(f'Arquivo gerado com sucesso: {nome_arquivo}')
    else:
        print(f'Endpoint sem dados: {endpoint}')
        input('ENTER')
else:
    print(f'Erro de Autenticação: {token}')
