from mysql.connector.errors import ProgrammingError
from db import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'


contato_grupo = {
    'Ana': 'Casa',
    'Bia': 'Trabalho',
    'Lucas Yuri': 'Trabalho',
    'Lu': 'Casa',
    'Gui': 'Trabalho',
    'Beca': 'Casa',
    'Pedro': 'Casa',
    'Luca': 'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('contatos associados')
