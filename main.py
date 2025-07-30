from biblioteca import Biblioteca

def menu():
    print("\n--- Sistema de Biblioteca ---")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Buscar por título")
    print("6. Buscar por autor")
    print("7. Relatório de empréstimos")
    print("0. Sair")

biblioteca = Biblioteca()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        biblioteca.cadastrar_livro(titulo, autor, isbn)
        print("Livro cadastrado com sucesso.")

    elif opcao == "2":
        nome = input("Nome do usuário: ")
        id_usuario = input("ID do usuário: ")
        biblioteca.cadastrar_usuario(nome, id_usuario)
        print("Usuário cadastrado com sucesso.")

    elif opcao == "3":
        isbn = input("ISBN do livro: ")
        id_usuario = input("ID do usuário: ")
        if biblioteca.emprestar_livro(isbn, id_usuario):
            print("Livro emprestado com sucesso.")
        else:
            print("Erro: livro indisponível ou não encontrado.")

    elif opcao == "4":
        isbn = input("ISBN do livro: ")
        if biblioteca.devolver_livro(isbn):
            print("Livro devolvido com sucesso.")
        else:
            print("Erro: livro não encontrado ou não está emprestado.")

    elif opcao == "5":
        titulo = input("Digite o título: ")
        encontrados = biblioteca.buscar_por_titulo(titulo)
        for livro in encontrados:
            print(livro)

    elif opcao == "6":
        autor = input("Digite o autor: ")
        encontrados = biblioteca.buscar_por_autor(autor)
        for livro in encontrados:
            print(livro)

    elif opcao == "7":
        print("\n--- Empréstimos Atuais ---")
        for entrada in biblioteca.relatorio_emprestimos():
            print(entrada)

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")
