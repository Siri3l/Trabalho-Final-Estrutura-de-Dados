from livro import Livro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = {}  # isbn: id_usuario

    def cadastrar_livro(self, titulo, autor, isbn):
        self.livros.append(Livro(titulo, autor, isbn))

    def cadastrar_usuario(self, nome, id_usuario):
        self.usuarios.append(Usuario(nome, id_usuario))

    def emprestar_livro(self, isbn, id_usuario):
        for livro in self.livros:
            if livro.isbn == isbn and not livro.emprestado:
                livro.emprestado = True
                self.emprestimos[isbn] = id_usuario
                return True
        return False

    def devolver_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn and livro.emprestado:
                livro.emprestado = False
                self.emprestimos.pop(isbn, None)
                return True
        return False

    def buscar_por_titulo(self, titulo):
        return [livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [livro for livro in self.livros if autor.lower() in livro.autor.lower()]

    def relatorio_emprestimos(self):
        relatorio = []
        for isbn, id_usuario in self.emprestimos.items():
            livro = next((l for l in self.livros if l.isbn == isbn), None)
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if livro and usuario:
                relatorio.append(f"{livro.titulo} emprestado para {usuario.nome}")
        return relatorio
