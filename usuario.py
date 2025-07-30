import random

# Conjunto global para garantir que não haja repetição de IDs
ids_usados = set()


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id_usuario = self._gerar_id_unico()

    def _gerar_id_unico(self):
        while True:
            novo_id = random.randint(1000, 9999)
            if novo_id not in ids_usados:
                ids_usados.add(novo_id)
                return novo_id

    def __str__(self):
        return f"👤 {self.nome} | ID: {self.id_usuario}"
