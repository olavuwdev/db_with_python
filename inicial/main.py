#importar conector
import mysql.connector

#estabelecer conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='deposito'
)
#criar o cursor
cursor = conexao.cursor()

#Função de laço para cadastrar item
while True:
    resp = input("Deseja cadastrar? (s/n): ")
    resp.lower()
    if resp ==  "n" or "não" or 'nao':
        break
    descricao = input('Descrição: ')
    posicao = input("Posição: ")
    cursor.execute(f'''INSERT INTO itens VALUES(null, '{descricao}', '{posicao}'); ''')
    print('Inserido com sucesso!')

while True:
    #Solicitar digitação do item a localizar
    item = input('Qual item do banco deseja localizar?')
    pos = input('Qual posição?')
    

    #executando a consulta
    cursor.execute(f"""SELECT * FROM itens WHERE descricao LIKE "%{item}%" AND posicao LIKE "%{pos}%"; """)

    #processar todos os registros do cursor
    dados = cursor.fetchall()

    #Exibir todos os dados do cursos
    '''for linha in cursor:
        print(linha) 
    '''

    #exibir dados com mais organização
    """for linha in cursor:
        print("Codigo:", linha[0])    
        print("Descrição:", linha[1])    
        print("Posição:", linha[2])    
        print("--------------------")    """

    for linha in dados:
        print("Codigo: ", linha[0], " | ", "Decrição: ", linha[1]," | " "posição: ", linha[2])  
        print(len(dados), "itens encontrados") 
    ask = input('Deseja fazer nova pesquisa?(S/N)')
    if ask == "Nao" or "Não" or "N":    
        break


#Retornar qts itens afetados no ultimo comando
#print(cursor.rowcount, "itens encontrados.")