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

def listar():
    print(" == LISTA DE LIVROS == ")
    
    cursor.execute("SELECT * FROM livros")
    for linha in cursor:
        print(f"=====| {linha[1]} |======= ")
        print("Codigo: ", linha[0])
        print("Titulo: ", linha[1])
        print("Autor: ", linha[2])
        print("Preço: ", linha[3])
        print("==========================")


def pesquisar():
    titulo = input("Titulo do Livro:")        
    autor = input("Autor do Livro:")
        
    
    cmd = f''' SELECT * FROM livros WHERE titulo LIKE '%{titulo}%' AND autor LIKE '%{autor}%' '''
    cursor.execute(cmd)
    for linha in cursor:
        print(f"=====| {linha[1]} |======= ")
        print("Codigo: ", linha[0])
        print("Titulo: ", linha[1])
        print("Autor: ", linha[2])
        print("Preço: ", linha[3])
        print("==========================")   



def alterar():
    cursor.execute("SELECT * FROM livros;")
    print('+_+_+_+_++_+ TABELA LIVROS _+_+_+_+_+_')
    for linha in cursor:
        print(linha)
    cod = input('Qual codigo do livro?')
    cursor.execute("SELECT * FROM livros WHERE codigo = "+ cod)
    #############  CONVERTE CONSULTA EM UMA LISTA #######################
    dados = cursor.fetchall()
    if len(dados) == 0:
        print("Item não encontrado!")
    else:
        print("===== DADOS DO LIVRO =====")
        print("Titulo:", dados[0][1])
        print("Autor:", dados[0][2])
        print("preco:", dados[0][3])
        escolha = input("Qual coluna deseja alterar: ")
        valor = input("Qual o novo {escolha}? ")
    
        cursor.execute(
        f'''UPDATE livros SET '{escolha}' = '{valor}' where codigo = '{cod}' ;''')

        conexao.commit()
        print("Alterado com sucesso!")




while True:
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Pesquisar")
    print("4. Alterar")
    print("5. SAIR")
    opção = input("Opção: ")
    if opção == '1':
        cadastro()
    elif opção == '2':
        listar()
    elif opção == '3':
        pesquisar()        
    elif opção == '4':
        alterar()
    elif opção == '5':
        print("Ate a proximo!")
        break
