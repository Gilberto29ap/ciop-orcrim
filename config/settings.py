from config.secrets import api_secret, id
client_secret = api_secret
client_id = id
token_url = "https://hmlsegurancaorcrim.mj.gov.br/auth/realms/hmlorcrim/protocol/openid-connect/token"
scopes = 'openid profile orcrim-backend'
API_BASE_URL = "https://hmlorcrim.mj.gov.br/backend-orcrim"