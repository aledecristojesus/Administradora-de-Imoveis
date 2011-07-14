#!/usr/bin/env python
# encoding: utf-8


class Endereco(object):

    def __init__(self, rua, numero, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
