import pandas as pd
uf_data = pd.read_csv("./data/uf.csv")

class Localizacao:
    id:int = None
    sigla:str = None
    nome:str = None
    regiao:str = None

    def __init__(self, data:pd.DataFrame) -> None:
        self.id = data["cod"]
        self.sigla = data["sigla"]
        self.nome = data["nome"]
        self.regiao = data["regiao"]

    def get_insert_str(self) -> str:
        return "INSERT INTO dim_localizacao (id, sigla, nome, regiao) VALUES({id}, '{sigla}', '{nome}', '{regiao}');".format(id=self.id, sigla=self.sigla, nome=self.nome, regiao=self.regiao)

class Tempo:
    id:int = None
    mes:int = None
    ano:int = None
    trimestre:int = None
    
    def __init__(self, data:pd.DataFrame) -> None:
        self.mes = int(data['mes'])
        self.ano = int(data['ano'])
        if self.mes <= 3:
            self.trimestre = 1
        elif self.mes <= 6:
            self.trimestre = 2
        elif self.mes <= 9:
            self.trimestre = 3
        else:
            self.trimestre = 4
            
    def check_if_valid(self, existent_list) -> None:
        valid = True
        for item in existent_list:
            if self.mes == item.mes and self.ano == item.ano:
                valid = False
                break
        return valid

    
    def get_same(self, existent_list):
        for item in existent_list:
            if self.mes == item.mes and self.ano == item.ano:
                return item
    
    def get_insert_str(self) -> str:
        return "INSERT INTO dim_tempo (id, mes, ano, trimestre) VALUES({id}, {mes}, {ano}, {trimestre});".format(id=self.id, mes=self.mes, ano=self.ano, trimestre=self.trimestre)

class Setor:
    id:int = None
    nome:str = None
    
    def __init__(self, data:pd.DataFrame) -> None:
        self.nome = data['tipo_consumo']

    def check_if_valid(self, existent_list) -> None:
        valid = True
        for item in existent_list:
            if self.nome == item.nome:
                valid = False
                break
        return valid

    def get_same(self, existent_list):
        for item in existent_list:
            if self.nome == item.nome:
                return item
    
    def get_insert_str(self) -> str:
        return "INSERT INTO dim_setor (id, nome) VALUES ({id}, '{nome}');".format(id=self.id, nome=self.nome)


class Fato:
    id:int = None
    consumo:float = None
    num_consumidores:float =  None
    fk_tempo:int = None
    fk_local:int = None
    fk_setor:int = None

    def __init__(self, tempo, local, setor, data:pd.DataFrame) -> None:
        self.fk_tempo = tempo
        self.fk_local = local
        self.fk_setor = setor
        self.consumo = data['consumo']
        self.num_consumidores = data['numero_consumidores'] or 'null'
        if self.num_consumidores == 'None':
            self.num_consumidores = 'null'
    def get_insert_str(self) -> str:
        return "INSERT INTO fato_consumo (id, consumo, num_consumidores, fk_tempo, fk_local, fk_setor) VALUES ({id}, {consumo}, {num_consumidores}, {tempo}, {local}, {setor});".format(id=self.id, consumo=self.consumo, num_consumidores=self.num_consumidores or 'null', tempo=self.fk_tempo, local=self.fk_local, setor=self.fk_setor)