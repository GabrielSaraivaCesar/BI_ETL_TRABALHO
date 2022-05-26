import pandas as pd
import tables
import database
import numpy as np


DB = database.Database()
_data = pd.read_csv("./data/energia.csv")
_data = _data.replace({np.nan: None})
_uf_data = pd.read_csv("./data/uf.csv")
# print(data.loc[data["sigla_uf"] == "RO"])
local = [
    tables.Localizacao(row) for row in _uf_data.to_dict('records')
]
fato = []
tempo = []
setor = []

for row in _data.to_dict('records'):
    tempo_row = tables.Tempo(row)
    if tempo_row.check_if_valid(tempo):
        tempo_row.id = len(tempo)
        tempo.append(tempo_row)
    else:
        tempo_row = tempo_row.get_same(tempo)

    setor_row = tables.Setor(row)
    if setor_row.check_if_valid(setor):
        setor_row.id = len(setor)
        setor.append(setor_row)
    else:
        setor_row = setor_row.get_same(setor)
    
    local_row = None
    for l in local:
        if l.sigla == row['sigla_uf']:
            local_row = l
    
    if local_row is not None:
        fato_row = tables.Fato(tempo_row.id, local_row.id, setor_row.id, row)
        fato_row.id = len(fato)
        fato.append(fato_row)
    

for l in local:
    DB.cursor.execute(l.get_insert_str())
for t in tempo:
    DB.cursor.execute(t.get_insert_str())
for s in setor:
    DB.cursor.execute(s.get_insert_str())
for f in fato:
    DB.cursor.execute(f.get_insert_str())

DB.connection.commit()


