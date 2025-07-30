class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) - {status}"
