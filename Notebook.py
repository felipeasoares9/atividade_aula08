from Produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        print(f"\nModelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.preco}\nCategoria: {self.categoria}\nTempo de bateria: {self.__tempoDeBateria} horas \n")

    def setInformacoes(self):
        self.__tempoDeBateria = int(input("Setar tempo de bateria: "))
        print(f"Tempo de bateria: {self.__tempoDeBateria} horas\n")

    def cadastrar(self):
        print(f"Notebook cadastrado com sucesso!\nModelo: {self.modelo}\nTempo de bateria: {self.__tempoDeBateria} horas\n")