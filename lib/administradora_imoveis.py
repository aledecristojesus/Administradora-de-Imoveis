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

    def comprar_imovel(self, imovel, preco_compra, preco_minimo_venda):
        imovel.antigo_proprietario = imovel.proprietario
        imovel.proprietario = "Imortal"
        imovel.preco_compra = preco_compra
        imovel.preco_minimo_venda = preco_minimo_venda
        self.imoveis_comprados.append(imovel)

    def vender_imovel(self, imovel, novo_proprietario, preco_venda):
        imovel.proprietario = novo_proprietario
        imovel.preco_venda = preco_venda
        self.imoveis_vendidos.append(imovel)
        self.imoveis_comprados.remove(imovel)

    def monitorar_imovel(self, imovel):
        self.imoveis_monitorados.append(imovel)

    def emitir_relacao_de_imoveis_disponiveis(self):
        # relatorio = []
        # for imovel in self.imoveis_comprados:
        #     relatorio.append((imovel.endereco, imovel.area, imovel.descricao, imovel.antigo_proprietario, imovel.preco_minimo_venda))
        # return relatorio
        # refatorar
        return map((lambda imovel: (imovel.endereco, imovel.area, imovel.descricao, imovel.antigo_proprietario, imovel.preco_minimo_venda)), self.imoveis_comprados)

    def emitir_relacao_de_imoveis_vendidos_por_bairro(self):
        relatorio = {}
        for imovel in self.imoveis_vendidos:
            if imovel.endereco.bairro not in relatorio.keys(): relatorio[imovel.endereco.bairro] = []
            relatorio[imovel.endereco.bairro].append((imovel.endereco.bairro, imovel.antigo_proprietario, imovel.proprietario, imovel.preco_venda, imovel.preco_compra))
        return relatorio

    def emitir_relacao_de_compradores_recorrentes(self):
        relatorio = []
        compradores = map((lambda imovel: imovel.proprietario), self.imoveis_vendidos)
        for comprador in compradores:
            if compradores.count(comprador) > 1:
                relatorio.append((comprador.nome, comprador.cpf, comprador.endereco, comprador.telefone))
                compradores.remove(comprador)
        return relatorio
