from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro


def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Listar livros")
        print("6. Listar usuários")
        print("7. Relatório de empréstimos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastro de Livro ---")
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            isbn = input("ISBN do livro: ")
            biblioteca.cadastrar_livro(titulo, autor, isbn)

        elif opcao == "2":
            print("\n--- Cadastro de Usuário ---")
            nome = input("Nome do usuário: ")
            biblioteca.cadastrar_usuario(nome)

        elif opcao == "3":
            print("\n--- Empréstimo de Livro ---")
            isbn = input("ISBN do livro: ")
            try:
                id_usuario = int(input("ID do usuário: "))
            except ValueError:
                print("ID inválido.")
                continue
            biblioteca.emprestar_livro(isbn, id_usuario)

        elif opcao == "4":
            print("\n--- Devolução de Livro ---")
            isbn = input("ISBN do livro: ")
            biblioteca.devolver_livro(isbn)

        elif opcao == "5":
            print("\n--- Lista de Livros ---")
            biblioteca.relatorio_livros()

        elif opcao == "6":
            print("\n--- Lista de Usuários ---")
            biblioteca.relatorio_usuarios()
        elif opcao == "7":
            biblioteca.relatorio_emprestimos()
        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
