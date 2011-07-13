#!/usr/bin/env python
# encoding: utf-8


from endereco import Endereco

class Imovel(Endereco):
    def __init__(self, area, descricao, preco_minimo, preco_compra, proprietario, endereco):
        self.area = area
        self.descricao = descricao        
        self.proprietario = proprietario
        self.preco_minimo = preco_minimo
        self.preco_compra = preco_compra
        self.preco_venda = None
        self.antigo_proprietario = None
        self.endereco = endereco

        
