import requests
from urllib.parse import urlencode
from typing import Union, Dict

def buscar_personalidade(data_inicio: str, data_fim: str, token: str) -> Union[Dict, str]:
    """
    Consulta a API do sistema ORCRIM para buscar informações sobre personalidades dentro de um intervalo de datas.

    Parâmetros:
    - data_inicio (str): A data de início para a busca, no formato 'DD/MM/AAAA HH:MM:SS.SSS'.
    - data_fim (str): A data de fim para a busca, no formato 'DD/MM/AAAA HH:MM:SS.SSS'.
    - token (str): Token de autorização para acessar a API.

    Retorna:
    - dict: Um objeto JSON com a resposta da API se a requisição for bem-sucedida e se a resposta puder ser processada corretamente.
    - str: Uma mensagem de erro contendo o código de status da resposta ou descrição do erro se a requisição falhar ou ocorrer um erro durante o processamento.

    Exemplo de uso:
    >>> data_inicio = '01/01/2023 00:00:00.000'
    >>> data_fim = '31/01/2024 00:00:00.000'
    >>> token = 'seu_token_aqui'
    >>> resultado = buscar_personalidade(data_inicio, data_fim, token)
    >>> print(resultado)

    Nota: Esta função depende da biblioteca 'requests' para fazer a requisição HTTP e 'urllib.parse' para codificação de URL.
    Assegure-se de que ambas as bibliotecas estejam instaladas e disponíveis no seu ambiente.
    """

    try:
        # Monta a URL com os parâmetros
        base_url = 'https://hmlorcrim.mj.gov.br/backend-orcrim/api/v1/personalidade'
        parametros = {'dataInicio': data_inicio, 'dataFim': data_fim}
        url_completa = f"{base_url}?{urlencode(parametros)}"

        # Define os cabeçalhos da requisição
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        # Faz a requisição GET
        response = requests.get(url_completa, headers=headers)

        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()  # Isso vai levantar uma exceção para respostas 4xx/5xx

        return response.json()  # Retorna a resposta em formato JSON

    except requests.exceptions.HTTPError as e:
        # Captura erros específicos de HTTP e retorna a mensagem
        return f'Erro HTTP: {e.response.status_code}, Mensagem: {e.response.text}'
    except requests.exceptions.RequestException as e:
        # Captura qualquer outra exceção de requests
        return f'Erro ao fazer a requisição: {e}'
    except Exception as e:
        # Captura qualquer outra exceção geral
        return f'Erro desconhecido: {str(e)}'
