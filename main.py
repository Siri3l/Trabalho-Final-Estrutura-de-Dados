from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro


def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Buscar livro por título")
        print("4. Buscar livro por autor")
        print("5. Emprestar livro")
        print("6. Devolver livro")
        print("7. Remover livro")
        print("8. Remover usuário")
        print("9. Listar livros")
        print("10. Listar usuários")
        print("11. Relatório de empréstimos")
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
            titulo = input("Digite parte ou o nome completo do título: ")
            biblioteca.buscar_livro_por_titulo(titulo)

        elif opcao == "4":
            autor = input("Digite parte ou o nome completo do autor: ")
            biblioteca.buscar_livro_por_autor(autor)

        elif opcao == "5":
            print("\n--- Empréstimo de Livro ---")
            isbn = input("ISBN do livro: ")
            try:
                id_usuario = int(input("ID do usuário: "))
            except ValueError:
                print("ID inválido.")
                continue
            biblioteca.emprestar_livro(isbn, id_usuario)

        elif opcao == "6":
            print("\n--- Devolução de Livro ---")
            isbn = input("ISBN do livro: ")
            biblioteca.devolver_livro(isbn)

        elif opcao == "7":
            print("\n--- Remover Livro ---")
            isbn = input("ISBN do livro a remover: ").strip()
            biblioteca.remover_livro(isbn)

        elif opcao == "8":
            print("\n--- Remover Usuário ---")
            try:
                id_usuario = int(input("ID do usuário a remover: "))
                biblioteca.remover_usuario(id_usuario)
            except ValueError:
                print("❌ ID inválido.")

        elif opcao == "9":
            print("\n--- Lista de Livros ---")
            biblioteca.relatorio_livros()

        elif opcao == "10":
            print("\n--- Lista de Usuários ---")
            biblioteca.relatorio_usuarios()

        elif opcao == "11":
            biblioteca.relatorio_emprestimos()

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
