from livro import Livro
from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = {}  # isbn: id_usuario

    def cadastrar_livro(self, titulo, autor, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                print("Erro: Já existe um livro cadastrado com esse ISBN.")
                return
        novo_livro = Livro(titulo, autor, isbn)
        self.livros.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, nome):
        novo_usuario = Usuario(nome)
        self.usuarios.append(novo_usuario)
        print(f"✅ {novo_usuario} cadastrado com sucesso.")
        return novo_usuario.id_usuario

    def emprestar_livro(self, isbn, id_usuario):
        isbn = isbn.strip()
        if not any(u.id_usuario == id_usuario for u in self.usuarios):
            print("❌ Usuário não encontrado.")
            return False

        for livro in self.livros:
            if livro.isbn == isbn and not livro.emprestado:
                livro.emprestado = True
                self.emprestimos[isbn] = id_usuario
                print(
                    f"📚 Livro '{livro.titulo}' emprestado para usuário ID {id_usuario}.")
                return True

        print("❌ Livro não disponível para empréstimo.")
        return False

    def devolver_livro(self, isbn):
        isbn = isbn.strip()
        for livro in self.livros:
            if livro.isbn == isbn and livro.emprestado:
                livro.emprestado = False
                self.emprestimos.pop(isbn, None)
                print(f"📦 Livro '{livro.titulo}' devolvido com sucesso.")
                return True

        print("❌ Livro não encontrado ou não está emprestado.")
        return False

    def buscar_por_titulo(self, titulo):
        return [livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [livro for livro in self.livros if autor.lower() in livro.autor.lower()]

    def relatorio_emprestimos(self):
        print("📑 Relatório de Empréstimos:")
        for isbn, id_usuario in self.emprestimos.items():
            livro = next((l for l in self.livros if l.isbn == isbn), None)
            usuario = next(
                (u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if livro and usuario:
                print(
                    f"- {livro.titulo} emprestado para {usuario.nome} (ID {usuario.id_usuario})")

    def relatorio_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("\n--- Relatório de Usuários ---")
        for usuario in self.usuarios:
            print(usuario)  # usa o __str__ da classe Usuario

    def relatorio_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("\n--- Relatório de Livros ---")
        for livro in self.livros:
            if livro.emprestado:
                id_usuario = self.emprestimos.get(livro.isbn)
                status = f"Emprestado para ID {id_usuario}"
            else:
                status = "Disponível"
            print(
                f"Título: {livro.titulo} | Autor: {livro.autor} | ISBN: {livro.isbn} | Status: {status}")
