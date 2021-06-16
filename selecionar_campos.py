from db import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    contatos = cursor.fetchall()

    for contato in contatos:
        print('\t'.join(str(campo) for campo in contato))
