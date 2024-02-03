from API_orcrim.token import get_token, check_token
from API_orcrim import buscar_personalidade

import json


# token = get_token()

# check_token(token)

# data_inicio = "01/01/2018 00:00:00.000"
# data_fim = "01/01/2024 00:00:00.000"

# personalidades = buscar_personalidade(data_inicio, data_fim, token)





# Salvar o resultado em um arquivo JSON
# caminho_do_arquivo = 'personalidades.json'

# with open(caminho_do_arquivo, 'r') as arquivo:
#     dados_carregados = json.load(arquivo)

# print(len(dados_carregados['data']))

from API_orcrim.token import TokenManager

# Usando a classe TokenManager com as configurações importadas
token_manager = TokenManager()