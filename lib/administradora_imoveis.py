#!/usr/bin/env python
# encoding: utf-8


class AdministradoraImovel(object):

    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.imoveis_comprados = []
        self.imoveis_vendidos = []
        self.imoveis_monitorados = []

    def comprar_imovel(self, imovel):
        imovel.antigo_proprietario = imovel.proprietario
        imovel.proprietario = "Imortal"
        self.imoveis_comprados.append(imovel)

    def vender_imovel(self, imovel, novo_proprietario, preco_venda):
        imovel.proprietario = novo_proprietario
        imovel.preco_venda = preco_venda
        self.imoveis_vendidos.append(imovel)
        self.imoveis_comprados.remove(imovel)

    def monitorar_imovel(self, imovel):
        self.imoveis_monitorados.append(imovel)
