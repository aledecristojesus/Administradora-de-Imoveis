#!/usr/bin/env python
# encoding: utf-8

import factory
# from spec_helper import *

class Proprietario(object):

    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco


class ProprietarioFactory(factory.Factory):
    nome = factory.Sequence(lambda n: 'Proprietario {0}'.format(n))


print ProprietarioFactory().nome
print ProprietarioFactory().nome
print ProprietarioFactory().nome
