import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2863',
    database='bdtest'
)

cursor = conexao.cursor()

#Create
nome_produto = str(input('Digite o nome do produto: '))
valor = int(input('Digite o valor do produto: '))
comando_sql1 = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
cursor.execute(comando_sql1)
conexao.commit() #Edita o banco de dados

#Read
comando_sql2 = 'SELECT * FROM vendas'
cursor.execute(comando_sql2)
resultado = cursor.fetchall() #Ler o banco de dados
print(resultado)

#Update
while True:
    update = str(input('Deseja atualizar o valor de algum produto [S/N]: ')).upper()

    if update == 'S':
        update_produto = str(input('Digite o nome do produto: '))
        update_valor = int(input('Digite o novo valor do produto: '))
        comando_sql3 = f'UPDATE vendas SET valor = {update_valor} WHERE nome_produto = "{update_produto}"'
        cursor.execute(comando_sql3)
        conexao.commit()
        break
    elif update == 'N':
        print('Okay!')
        break
    else:
        print('Por favor, insira os dados corretamente!')

#Delete
while True:
    delete = str(input('Deseja remover algum produto [S/N]: '))

    if delete == 'S':
        delete_produto = str(input('Digite o nome do produto que deseja remover: ')).upper()
        comando_sql4 = f'DELETE FROM vendas WHERE nome_produto = "{delete_produto}"'
        cursor.execute(comando_sql4)
        conexao.commit()
        break
    elif delete == 'N':
        print('Okay!')
        break
    else:
        print('Por favor, insira os dados corretamente')

cursor.close()
conexao.close()