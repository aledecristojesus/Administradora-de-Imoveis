#!/usr/bin/env python
# encoding: utf-8

class Imovel(object):
    
    def __init__(self,rua, numero, bairro, cidade, uf, cep, descricao, area):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.descricao = descricao
        self.area = area
        self.antigo_proprietario = None
        self.proprietario = "Imortal"
        self.preco_compra = None
        self.preco_minimo = None
        self.preco_venda = None
       

