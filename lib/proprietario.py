#!/usr/bin/env python
# encoding: utf-8


from endereco import Endereco

class Proprietario(object):

    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone 
        self.endereco = endereco
 
