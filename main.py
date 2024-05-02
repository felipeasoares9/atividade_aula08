from Categoria import Categoria
from Produto import Produto
from Notebook import Notebook
from Desktop import Desktop


if __name__ == "__main__":
    c1 = Categoria("modelo01", "Azul", 19.90, "18 polegadas", "01", "nome_teste")
    c1.cadastrar()
    n1 = Notebook("modelo02", "Preto", 1500.00, None, 6)
    n1.cadastrar()
    n1.getInformacoes()
    n1.setInformacoes()
    d1 = Desktop("modelo03", "Preto", 1500.00, None, "750W")
    d1.cadastrar()
    d1.getInformacoes()
    d1.setInformacoes()
