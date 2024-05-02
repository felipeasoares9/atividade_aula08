from Produto import Produto

class Categoria(Produto):
    def __init__(self, modelo, cor, preco, categoria, id, nome):
        super().__init__(modelo, cor, preco, categoria)
        self.id = id
        self.nome = nome

    def cadastrar(self):
        print(f"id: {self.id}\nnome:{self.nome}")