"# Din-micaEstoqueComHeran-aEPolimorfismo" 
# 🛒 Sistema de Estoque com Produtos Diversificados

Este projeto em Python simula um sistema de controle de estoque com diferentes tipos de produtos. Ele demonstra os conceitos de **herança**, **polimorfismo** e **aplicação de descontos** com base no tipo de produto.

## 📦 Classes

### `Produto`
Classe base que representa um produto genérico com:
- `nome`
- `preco`

Método:
- `mostrar_dados()`: Exibe o nome e o preço do produto.

---

### `ProdutoPerecivel(Produto)`
Herda de `Produto`. Representa produtos com data de validade.

Atributo adicional:
- `validade`

Método sobrescrito:
- `mostrar_dados()`: Exibe nome, preço e validade.

---

### `ProdutoNaoPerecivel(Produto)`
Herda de `Produto`. Representa produtos com material definido.

Atributo adicional:
- `material`

Método sobrescrito:
- `mostrar_dados()`: Exibe nome, preço e material.

---

### `ProdutoImportado(Produto)`
Herda de `Produto`. Representa produtos importados.

Atributo adicional:
- `pais_origem`

Método sobrescrito:
- `mostrar_dados()`: Exibe nome, preço e país de origem.

---

## 📉 Função de Desconto

```python
def aplicar_desconto(produto):
