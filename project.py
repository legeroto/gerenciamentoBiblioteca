print("Bem-vindo ao Sistema de Controle de livros do Leandro Geroto Soares!")

# CADASTRANDO UM LIVRO
def cadastrarlivro(id, listaLivro):
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("----------------- MENU CADASTRAR LIVRO ------------------")
    print(f"ID Livro: {id}")
    nome = input("Por favor, entre com o nome do livro: ")
    autor = input("Por favor, entre com o autor: ")
    editora = input("Por favor, entre com a editora: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    listaLivro.append(livro)
    print("Livro cadastrado com sucesso!")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("-------------------- MENU PRINCIPAL ---------------------")

# CONSULTANDO LIVROS
def consultarlivro(listaLivro):
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("----------------- MENU CONSULTA LIVRO -------------------")
    opcao = input("Qual opção deseja?\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n")
    if opcao == '1':
        for livro in listaLivro:
            print("id:", livro['id'])
            print("nome:", livro['nome'])
            print("autor:", livro['autor'])
            print("editora:", livro['editora'])
            print("--------------------------------------------------")
    elif opcao == '2':
        idLivro = int(input("Digite o id do livro: "))
        for livro in listaLivro:
            if livro['id'] == idLivro:
                print("id:", livro['id'])
                print("nome:", livro['nome'])
                print("autor:", livro['autor'])
                print("editora:", livro['editora'])
                print("--------------------------------------------------")
                return
        print("Livro não encontrado.")
    elif opcao == '3':
        autor = input("Digite o nome do autor: ")
        for livro in listaLivro:
            if livro['autor'] == autor:
                print("id:", livro['id'])
                print("nome:", livro['nome'])
                print("autor:", livro['autor'])
                print("editora:", livro['editora'])
                print("--------------------------------------------------")
    elif opcao == '4':
        return
    else:
        print("Opção inválida")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

# REMOVENDO LIVROS
def removerlivro(listaLivro):
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("------------------ MENU REMOVER LIVRO -------------------")
    idLivro = int(input("Digite o id do livro a ser removido: "))
    for livro in listaLivro:
        if livro['id'] == idLivro:
            listaLivro.remove(livro)
            print("Livro removido com sucesso.")
            return
    print("Livro não encontrado.")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

# EXIBINDO O MENU PRINCIPAL
def main():
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("-------------------- MENU PRINCIPAL ---------------------")
    listaLivro = []
    id_livro_global = 0
    while True:
        opcao = input("Escolha a opção desejada:\n1. Cadastrar Livro\n2. Consultar Livro(s)\n3. Remover Livro\n4. Sair\n")
        if opcao == '1':
            id_livro_global += 1
            cadastrarlivro(id_livro_global, listaLivro)
        elif opcao == '2':
            consultarlivro(listaLivro)
        elif opcao == '3':
            removerlivro(listaLivro)
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida")
            print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

# CHAMADA PARA EXECUÇÃO DO CÓDIGO
if __name__ == "__main__":
    main()
