import json
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Pessoa:

    """
    Representa uma pessoa com atributos detalhados, incluindo informações pessoais,
    documentos e associações.

    Atributos:
        nome (str): Nome da pessoa.
        dataNascimento (str): Data de nascimento da pessoa no formato 'AAAA-MM-DD'.
        nomeMae (str): Nome da mãe da pessoa.
        nomePai (str): Nome do pai da pessoa.
        obito (bool): Indica se a pessoa está morta.
        municipio (Municipio): O município de residência da pessoa.
        uf (Uf): A unidade federativa de residência da pessoa.
        sexo (Sexo): O sexo da pessoa.
        nacionalidade (Nacionalidade): A nacionalidade da pessoa.
        alcunhas (list[Alcunhas]): Lista de alcunhas/apelidos da pessoa.
        cpfs (list[Cpfs]): Lista de CPFs da pessoa.
        rgs (list[Rgs]): Lista de RGs da pessoa.
        orcrim (list[Orcrim]): Lista de associações criminosas da pessoa.

    Métodos:
        to_dict: Retorna um dicionário representando a pessoa.
        to_json: Retorna uma string JSON representando a pessoa.
    """

    class Municipio:

        """
        Representa um município.

        Atributos:
            id (int): ID do município.
            nome (str): Nome do município.
        """

        def __init__(self, id, nome):
            self.id = id
            self.nome = nome

        def to_dict(self):
            return vars(self)
        
    class Uf:


        def __init__(self, id, nome, sigla):
            self.id = id
            self.nome = nome
            self.sigla = sigla

        def to_dict(self):
            return vars(self)
        
    class Alcunhas:
        def __init__(self, alcunha, dataAlcunha):
            self.alcunha = alcunha
            self.dataAlcunha = dataAlcunha
            
        def to_dict(self):
            return vars(self)
        
    class Cpfs:
        def __init__(self, cpf):
            self.cpf = cpf

        def to_dict(self):
            return vars(self)
        
    class Rgs:
        def __init__(self, rg, ufRg):
            self.rg = rg
            self.ufRg = ufRg

        
        def to_dict(self):
            # Cria uma cópia do dicionário de atributos para não alterar o objeto original
            rgs_dict = vars(self).copy()
            # Atualiza a cópia do dicionário com a representação em dicionário de UFRg
            rgs_dict['ufRg'] = self.ufRg.to_dict()
            return rgs_dict
        

    class Sexo:
        def __init__(self, id, nome):
            self.id = id
            self.nome = nome

        def to_dict(self):
            return vars(self)


    class Orcrim:
        def __init__(self, id, nome, sigla):
            self.id = id
            self.nome = nome
            self.sigla = sigla

        def to_dict(self):
            return vars(self)
        
    class Nacionalidade:
        def __init__(self, id, nome):
            self.id = id
            self.nome = nome

        def to_dict(self):
            return vars(self)


    
    def __init__(self, nome=None, dataNascimento=None, nomeMae=None, nomePai=None, obito=None, municipio_id=None, municipio_nome=None,
                 uf_id=None, uf_nome=None, uf_sigla=None, sexo_id=None, sexo_nome=None, nacionalidade_id=None, nacionalidade_nome=None,
                 alcunhas=None, cpfs=None, rgs=None, orcrim=None):
        
        """
        Inicializa uma instância da classe Pessoa com informações detalhadas.

        Todos os parâmetros são opcionais, permitindo a criação de uma instância de Pessoa
        com diferentes níveis de detalhamento.
        """
        logging.info(f"Criando nova instância de Pessoa: {nome}") 
        self.nome = nome
        self.dataNascimento = dataNascimento if dataNascimento else 'Data Desconhecida'
        self.nomeMae = nomeMae if nomeMae else 'Desconhecido'
        self.nomePai = nomePai if nomePai else 'Desconhecido'
        self.obito = obito if obito is not None else "N"  # Assume False se obito não for fornecido

        # Para os atributos compostos por outras classes, verifica a existência dos dados antes da criação.
        self.municipio = self.Municipio(municipio_id, municipio_nome) if municipio_id and municipio_nome else None
        self.uf = self.Uf(uf_id, uf_nome, uf_sigla) if uf_id and uf_nome and uf_sigla else None
        self.sexo = self.Sexo(sexo_id, sexo_nome) if sexo_id and sexo_nome else None
        self.nacionalidade = self.Nacionalidade(nacionalidade_id, nacionalidade_nome) if nacionalidade_id and nacionalidade_nome else None

        # Para listas, mantém a lógica de verificação e criação a partir dos dados fornecidos.
        self.alcunhas = [self.Alcunhas(a['alcunha'], a['dataAlcunha']) for a in alcunhas] if alcunhas else []
        self.cpfs = [self.Cpfs(c['cpf']) for c in cpfs] if cpfs else []
        self.rgs = [self.Rgs(rg['rg'], self.Uf(rg['ufRg']['id'], rg['ufRg']['nome'], rg['ufRg']['sigla'])) for rg in rgs] if rgs and self.uf else []
        self.orcrim = [self.Orcrim(o['id'], o['nome'], o['sigla']) for o in orcrim] if orcrim else []

    def to_dict(self):

        """
        Converte a pessoa e seus atributos para um dicionário.

        Retorna:
            dict: Um dicionário contendo todos os atributos da pessoa e seus valores,
            incluindo os detalhes das entidades relacionadas como listas de dicionários.
        """
        pessoa_dict = {
        "nome": self.nome,
        "dataNascimento": self.dataNascimento,
        "nomeMae": self.nomeMae,
        "nomePai": self.nomePai,
        "obito": self.obito,
        "municipio": self.municipio.to_dict() if self.municipio else None,
        "uf": self.uf.to_dict() if self.uf else None,
        "sexo": self.sexo.to_dict() if self.sexo else None,
        "nacionalidade": self.nacionalidade.to_dict() if self.nacionalidade else None,
        "alcunhas": [a.to_dict() for a in self.alcunhas],
        "cpfs": [c.to_dict() for c in self.cpfs],
        "rgs": [r.to_dict() for r in self.rgs],
        "orcrims": [o.to_dict() for o in self.orcrim],
    }
        return pessoa_dict

    def to_json(self):
        """
        Serializa a pessoa e seus atributos para uma string JSON.

        Retorna:
            str: Uma representação JSON da pessoa e seus atributos, incluindo as entidades
            relacionadas.
        """

        return json.dumps({"data": [self.to_dict()]}, ensure_ascii=False, indent=2)