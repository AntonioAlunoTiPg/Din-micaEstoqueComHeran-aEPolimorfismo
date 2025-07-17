class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_dados(self):
        print(f"{self.nome} custa R${self.preco:.2f}")


class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, validade):
        super().__init__(nome, preco)
        self.validade = validade

    def mostrar_dados(self):
        print(f"{self.nome} custa R${self.preco:.2f} e vence em {self.validade}")


class ProdutoNaoPerecivel(Produto):
    def __init__(self, nome, preco, material):
        super().__init__(nome, preco)
        self.material = material

    def mostrar_dados(self):
        print(f"{self.nome} custa R${self.preco:.2f} e é feito de {self.material}")


# NOVA CLASSE: ProdutoImportado
class ProdutoImportado(Produto):
    def __init__(self, nome, preco, pais_origem):
        super().__init__(nome, preco)
        self.pais_origem = pais_origem

    def mostrar_dados(self):
        print(f"{self.nome} custa R${self.preco:.2f} e veio de {self.pais_origem}")


# Exemplos
p = Produto("Caderno", 12.50)
p.mostrar_dados()

banana = ProdutoPerecivel("Banana", 5.00, "2025-08-01")
cadeira = ProdutoNaoPerecivel("Cadeira", 120.00, "Madeira")

banana.mostrar_dados()
cadeira.mostrar_dados()

# Criando produto importado
vinho = ProdutoImportado("Vinho Italiano", 150.00, "Itália")

# Adicionando todos ao estoque
estoque = [
    Produto("Garrafa", 20.00),
    ProdutoPerecivel("Leite", 4.99, "2025-07-30"),
    ProdutoNaoPerecivel("Mesa", 250.00, "Metal"),
    vinho  # ProdutoImportado incluído
]

# Mostrando dados dos produtos no estoque
for item in estoque:
    item.mostrar_dados()

# Função para aplicar desconto com 15% para ProdutoImportado
def aplicar_desconto(produto):
    if isinstance(produto, ProdutoPerecivel):
        produto.preco *= 0.9  # 10% de desconto
    elif isinstance(produto, ProdutoNaoPerecivel):
        produto.preco *= 0.95  # 5% de desconto
    elif isinstance(produto, ProdutoImportado):
        produto.preco *= 0.85  # 15% de desconto
    else:
        produto.preco *= 0.98  # 2% para os demais
    produto.mostrar_dados()

# Aplicando desconto
for item in estoque:
    aplicar_desconto(item)

    