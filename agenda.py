escolha = 0
contatos = {}
favoritos = {}


def adicionar_contato(): #1
    nome = input("Adicione o nome do contato: ")
    telefone = input("Adicione o telefone do contato: ")
    if (len(str(telefone)) != 11):
        print("Valor de telefone inválido.")
    else:
        contatos[nome] = telefone
        favorito = input("O contato deve ser adicionado a lista de favoritos? responda com sim caso deva: ")
        if (favorito == "sim"):
            favoritos[nome] = telefone
        
def listar_contatos(): #2
    print("Lista de contatos:\n",contatos)
    
def Buscar_contato(): #3
    nbusc = input("Qual o nome do contato que você deseja buscar?: ")
    tbusc = input("Qual o telefone desse contato?: ")
    if (nbusc in contatos) == True:
        print("O contato {{",nbusc,": ",tbusc,"}} se encontra na sua lista de contatos.")
        print("Contatos da sus lista: ",contatos)
    else:
        print("O contato descrito não se encontra presente nos seus contatos.")
        print("Contatos da sus lista: ",contatos)
        
def atualizar(): #4
    nnome = input("Qual o nome do contato que você deseja atualizar?: ")
    ntelefone = input("Qual o telefone desse contato?: ")
    if nnome in contatos:
        nat = input("Escreva o nome atualizado do contato: ")
        tat = input("Escreva o telefone atualizado do contato: ")
        del contatos[nnome]
        contatos[nat] = tat
        print("Contato atualizado.")
    else:
        print("Este contato não se encontra em sua lista de contatos.")
        
def remover_contato(): #5
    ndel = input("Qual o nome do contato que você deseja deletar?: ")
    if ndel in contatos:
        del contatos[ndel]
        print("Contato deletado da lista de contatos.")
    else:
        print("O contato descrito não se encontra presente nos seus contatos.")
        
def favoritar():
    resp = input("você deseja favoritar ou desfavoritar um contato? favoritar = 1, desfavositar = 2: ")
    if resp == "1":
        print("Lista de contatos:\n ",contatos,"\n")
        nf = input("Qual o nome do contato que você deseja favoritar?: ")
        tf = input("Qual o telefone desse contato?: ")
        if (nf in contatos) == True:
            favoritos[nf] = tf
            print("Adicionado a lista de favoritos.")
        else:
            print("O contato descrito não se encontra presente nos seus contatos.")
    if resp == "2":
        print("Lista de contatos:\n ",contatos,"\n")
        nf = input("Qual o nome do contato que você deseja desfavoritar?: ")
        if (nf in contatos) == True:
            del favoritos[nf]
            print("removido da lista de favoritos.")
        else:
            print("O contato descrito não se encontra presente nos seus contatos.")
    else:
        print("Resposta inválida.")
        
    
def list_fav():
    print("Lista de favoritos:\n",favoritos)
    
        
        


while (escolha != 8):

    print("AGENDA DE CONTATOS\n1. Adicionar contato\n2. Listar contatos\n3. Buscar contato\n4. Atualizar contato\n5. Remover contato")
    print("6. Favoritar/Desfavoritar contato\n7. Listar contatos favoritos\n8. Sair\nEscolha uma opção:")
    escolha = input()
    
    if escolha == "1":
        adicionar_contato()
        
    if escolha == "2":
        listar_contatos()
        
    if escolha == "3":
        Buscar_contato()
        
    if escolha == "4":
        atualizar()
        
    if escolha == "5":
        remover_contato()
        
    if escolha == "6":
        favoritar()
        
    if escolha == "7":
        list_fav()
        
    if escolha == "8":
        print("Programa encerrado.")
        
    else:
        print("Escolha inválida.")