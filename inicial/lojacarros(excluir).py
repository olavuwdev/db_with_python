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
cod = input('Qual codigo deseja excluir?')

cursor.execute("SELECT * FROM carros WHERE codigo = "+ cod)
#############  CONVERTE CONSULTA EM UMA LISTA #######################
dados = cursor.fetchall()
if len(dados) == 0:
    print("Item não encontrato!")
else:
    print(dados)
    ex_result = input('Deseja excluir?')
    if ex_result == "s" or "sim":
        cursor.execute("DELETE FROM carros WHERE codigo = " + cod)
        conexao.commit()
        print(dados)
        print("Excluido com sucesso!")
    else:
        print("Item não excluido, programa finalizado!")

