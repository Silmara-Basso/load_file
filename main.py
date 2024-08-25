

produto1: dict = {
    "nome":"sapato",
    "quantidade":30,
    "valor":10.35,
    "disponibilidade": True
}

produto2: dict = {
    "nome" : "telefisao",
    "quantidade": 35,
    "valor": 1000,
    "disponibilidade": False
}

carrinho : list = []
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)