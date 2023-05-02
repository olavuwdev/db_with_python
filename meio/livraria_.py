#importar conector
import mysql.connector

#estabelecer conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='livraria'
)
#criar o cursor
cursor = conexao.cursor()

def cadastro():
    print("== CADASTRO LIVRO ==")
    titulo = input("Titulo do livro:")
    autor = input("Autor do livro:")
    preco = input("Preço do livro:")
    cmd = "INSERT INTO livros VALUES (null, %s, %s, %s)"
    cursor.execute(cmd, (titulo, autor, preco))
    conexao.commit()
    input("Inserido com sucesso!")




while True:
    print("1. Cadastrar")
    print("5. SAIR")
    opção = input("Opção: ")
    if opção == '1':
        cadastro()
    elif opção == '5':
        print("Ate a proximo!")
        break
