from Produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self.__potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        print(f"\nModelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.preco}\nCategoria: {self.categoria}\nPotencia da fonte: {self.__potenciaDaFonte}W\n")

    def setInformacoes(self):
        self.__potenciaDaFonte = int(input("Setar potencia da fonte: "))
        print(f"Potencia da fonte: {self.__potenciaDaFonte}W")

    def cadastrar(self):
        print(f"Desktop cadastrado com sucesso!\nModelo: {self.modelo}\nPotencia da fonte: {self.__potenciaDaFonte}W")