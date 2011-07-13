#!/usr/bin/env python
# encoding: utf-8

class AdministradoraImovel(object):
    
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco 
        self.imoveis_comprados = []
 
    def comprar_imovel(self, imovel):
        imovel.antigo_proprietario = imovel.proprietario
        imovel.proprietario = "Imortal"
        self.imoveis_comprados.append(imovel)
        
