from db import nova_conexao

sql = "SELECT nome FROM contatos ORDER BY nome DESC"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(registro[0] for registro in cursor))
