#!/usr/bin/env python
# encoding: utf-8


class Imovel(object):
    def __init__(self, area, descricao, proprietario, endereco):
        self.area = area
        self.descricao = descricao
        self.proprietario = proprietario
        self.endereco = endereco
        self.preco_minimo_venda = None
        self.preco_compra = None
        self.preco_venda = None
        self.antigo_proprietario = None
