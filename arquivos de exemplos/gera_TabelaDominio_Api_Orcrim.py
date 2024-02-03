from gets_api_orcrim import autenticar_usuario, busca_gets_sem_param
import json
# client_id do usuário e client_secret do usuário
user_hml = ''
password_hml = ''

# url de autenticação
url_autenticacao_hml = 'https://hmlsegurancaorcrim.mj.gov.br/auth/realms/hmlorcrim/protocol/openid-connect/token'

# Gera o token
token = autenticar_usuario(url_autenticacao_hml, user_hml, password_hml)

# url do ambiente da base de dados
base_url = "https://hmlorcrim.mj.gov.br/backend-orcrim/api/v1"

lista_endpoints_sem_parametros = {'/funcoes', '/instituicoes', '/nacionalidades', '/orcrims', '/qualificacao/naturezas',
                                  '/qualificacao/grupos', '/qualificacao/capitulos', '/qualificacao/titulos',
                                  '/qualificacao/legislacoes', '/sexos', '/tiposDocumentos', '/tiposEndereco',
                                  '/tiposFuncoesOrcrim', '/tiposProcedimentoCriminal', '/tiposRegimes',
                                  '/tiposUnidadesPrisionais', '/ufs', '/unidadesPrisionais'}
if token:
    for endpoint in lista_endpoints_sem_parametros:
        nome_arquivo = './json' + endpoint + '.json'
        print(nome_arquivo)
        dados = busca_gets_sem_param(token, base_url, endpoint)

        if dados:
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados, arquivo)
        else:
            print(f'Endpoint sem dados: {endpoint}')
            input('ENTER')

else:
    print(f'Erro de Autenticação: {token}')
    input('ENTER')
