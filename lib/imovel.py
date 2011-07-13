#!/usr/bin/env python
# encoding: utf-8


from endereco import Endereco

class Imovel(Endereco):
    def __init__(self, area, descricao, preco_minimo, preco_compra, antigo_proprietario, endereco):
        self.area = area
        self.descricao = descricao        
        self.proprietario = "Imortal"
        self.preco_minimo = preco_minimo
        self.preco_compra = preco_compra
        self.preco_venda = None
        self.antigo_proprietario = antigo_proprietario
        self.endereco = endereco
