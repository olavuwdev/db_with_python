#importar conector
import mysql.connector

#estabelecer conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lojacarros'
)
#criar o cursor
cursor = conexao.cursor()

#######################################################


cursor.execute("SELECT * FROM carros;")
print('+_+_+_+_++_+ TABELA CARROS _+_+_+_+_+_')
for linha in cursor:
    print(linha)
cod = input('Qual codigo deseja alterar?')
cursor.execute("SELECT * FROM carros WHERE codigo = "+ cod)
#############  CONVERTE CONSULTA EM UMA LISTA #######################
dados = cursor.fetchall()
if len(dados) == 0:
    print("Item não encontrado!")
else:
    print("codigo:", dados[0][0])
    print("fabricante:", dados[0][1])
    print("modelo:", dados[0][2])
    print("preco:", dados[0][3])
    coluna =input("Qual coluna deseja alterar?")
    valor =input("Qual novo valor?")
    
    cursor.execute(
    f'''UPDATE carros SET {coluna} = '{valor}' where codigo = '{cod}' ;''')

    conexao.commit()
    print("Alterado com sucesso!")
    print("codigo:", dados[0][0])
    print("fabricante:", dados[0][1])
    print("modelo:", dados[0][2])
    print("preco:", dados[0][3])
    