from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '98465-4321'),
    ('Bia', '98765-4321'),
    ('Luca', '98765-4361'),
    ('Lu', '98965-4321'),
    ('Gui', '98765-4341'),
    ('Beca', '92765-4321'),
    ('Pedro', '98765-7321'),

)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
