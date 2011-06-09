#!/usr/bin/env python
# encoding: utf-8

class Proprietario(object):
    def __init__(self, nome, cpf, rua, numero, bairro, cidade, uf, cep, telefone):
        self.nome = nome
        self.cpf = cpf
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.telefone = telefone

