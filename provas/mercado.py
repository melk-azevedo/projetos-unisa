class Produto:
    "Método construtor da classe produto"

    def __init__(self, produto: str, preco: str, estoque: int) -> None:
        self.produto = produto
        self.preco = preco
        self.estoque = estoque

    def toString(self):
        return f'''{self.produto} custa {self.preco}
 e tem {self.estoque} em estoque'''


class SuperMercado:
    produtos = []

    def adicionar_produtos(self, object):
        self.produtos.append(object)
        print('O produto foi adicionado com sucesso')


morangos = Produto('Morango', 'R$ 8,99', 8)
pera = Produto('Pera', 'R$ 1,99', 50)
arroz = Produto('Arroz', 'R$ 16,99', 37)

mercado = SuperMercado()
mercado.adicionar_produtos(morangos.toString())
mercado.adicionar_produtos(pera.toString())
mercado.adicionar_produtos(arroz.toString())


class Pedido:
    "Método construtor da classe pedido"

    def __init__(self, quantidade: int, item: str):
        self.quantidade = quantidade
        self.item = item

    def toString(self):
        return f'Você pediu {self.quantidade} unidades de {self.item}'


class Clientes:
    "Método construtor da classe Cliente"

    def __init__(self, nome, sobrenome, tel, email):
        self.nome = nome
        self.tel = tel
        self.email = email
        self.sobrenome = sobrenome

    def toString(self):
        return f'{self.nome} {self.sobrenome}, {self.tel}, {self.email}'


class Compras:
    itens = []

    def adicionar_item(self, object):
        self.itens.append(object)
        print('O item foi adicionado a sua sacola.')


pedido1 = Pedido(8, 'Morangos')
pedido2 = Pedido(3, 'Pera')

compra = Compras()
compra.adicionar_item(pedido1.toString())
compra.adicionar_item(pedido2.toString())
