from livro import Livro
from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = {}  # isbn: id_usuario

    def cadastrar_livro(self, titulo, autor, isbn):
        # Verifica se algum campo está vazio
        if not titulo.strip() or not autor.strip() or not isbn.strip():
            print("❌ Erro: Todos os campos devem ser preenchidos.")
            return

        # Verifica se o título e autor têm um tamanho mínimo
        if len(titulo.strip()) < 2:
            print("❌ Erro: O título do livro é muito curto.")
            return
        if len(autor.strip()) < 2:
            print("❌ Erro: O nome do autor é muito curto.")
            return

        # Verifica se o ISBN tem apenas dígitos (ou você pode permitir hífens com regex)
        if not isbn.isdigit():
            print("❌ Erro: O ISBN deve conter apenas números.")
            return

        # Verifica se o ISBN já existe
        for livro in self.livros:
            if livro.isbn == isbn:
                print("❌ Erro: Já existe um livro cadastrado com esse ISBN.")
                return

        # Se tudo estiver certo, cadastra o livro
        novo_livro = Livro(titulo.strip(), autor.strip(), isbn.strip())
        self.livros.append(novo_livro)
        print(f"✅ Livro '{titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, nome):
        nome = nome.strip()

        # Verifica se o nome está vazio
        if not nome:
            print("❌ Erro: O nome do usuário não pode estar vazio.")
            return

        # Verifica se o nome é muito curto
        if len(nome) < 2:
            print("❌ Erro: O nome deve ter pelo menos 2 caracteres.")
            return

        # Verifica se o nome contém apenas letras e espaços
        if not all(c.isalpha() or c.isspace() for c in nome):
            print("❌ Erro: O nome deve conter apenas letras e espaços.")
            return

        # Verifica se já existe um usuário com o mesmo nome (opcional)
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                print("❌ Erro: Já existe um usuário com esse nome.")
                return

        # Se passou todas as validações, cadastra o usuário
        novo_usuario = Usuario(nome)
        self.usuarios.append(novo_usuario)
        print(f"✅ {novo_usuario} cadastrado com sucesso.")
        return novo_usuario.id_usuario

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                if livro.emprestado:
                    print(
                        f"❌ O livro '{livro.titulo}' está emprestado e não pode ser removido.")
                    return
                self.livros.remove(livro)
                print(f"✅ Livro '{livro.titulo}' removido com sucesso.")
                return
        print("❌ Livro não encontrado.")

    def remover_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                if usuario.livros_emprestados:  # Verifica se há livros emprestados
                    print(
                        f"❌ O usuário '{usuario.nome}' possui livros emprestados e não pode ser removido.")
                    return
                self.usuarios.remove(usuario)
                print(f"✅ Usuário '{usuario.nome}' removido com sucesso.")
                return
        print("❌ Usuário com esse ID não foi encontrado.")

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

    def buscar_livro_por_titulo(self, titulo):
        encontrados = [
            livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]
        if encontrados:
            print("\n📚 Livros encontrados por título:")
            for livro in encontrados:
                print(livro)
        else:
            print("❌ Nenhum livro encontrado com esse título.")

    def buscar_livro_por_autor(self, autor):
        encontrados = [
            livro for livro in self.livros if autor.lower() in livro.autor.lower()]
        if encontrados:
            print("\n✍️ Livros encontrados por autor:")
            for livro in encontrados:
                print(livro)
        else:
            print("❌ Nenhum livro encontrado para esse autor.")

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
