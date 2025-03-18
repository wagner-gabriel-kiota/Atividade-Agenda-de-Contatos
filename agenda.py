escolha = 0
contatos = []
favoritos = []


def adicionar_contato(nome,telefone,favorito):
    contatos.append({nome:telefone})
    if favorito == "sim":
        favoritos.append({nome:telefone})


while (escolha != 8):

    print("AGENDA DE CONTATOS\n1. Adicionar contato\n2. Listar contatos\n3. Buscar contato\n4. Atualizar contato\n5. Remover contato")
    print("6. Favoritar/Desfavoritar contato\n7. Listar contatos favoritos\n8. Sair\nEscolha uma opção:")
    escolha = int(input())