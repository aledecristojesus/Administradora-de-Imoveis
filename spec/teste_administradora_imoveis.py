#!/usr/bin/env python
# encoding: utf-8

import unittest
from should_dsl import should
from administradora_imoveis import AdministradoraImovel
from endereco import Endereco
from proprietario import Proprietario
from imovel import Imovel

class TestAdministradora_Imoveis(unittest.TestCase):

    def test_inicializa_atributos(self):
        endereco = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        administradora_imovel.nome |should| equal_to("Imortal")
        administradora_imovel.cnpj |should| equal_to("45635656777")
        administradora_imovel.endereco |should| equal_to(endereco)
        administradora_imovel.imoveis_comprados |should| equal_to([])
        administradora_imovel.imoveis_vendidos |should| equal_to([])
        administradora_imovel.imoveis_monitorados |should| equal_to([])

    def test_comprar_imovel(self):        
        endereco = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel( 600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.comprar_imovel(imovel)
        administradora_imovel.imoveis_comprados[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_comprados[0].proprietario |should| equal_to("Imortal")
        administradora_imovel.imoveis_comprados[0].antigo_proprietario |should| equal_to(proprietario)

    def test_vender_imovel(self):
        endereco = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel( 600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.comprar_imovel(imovel)
        administradora_imovel.vender_imovel(imovel, proprietario, 60000.00)
        administradora_imovel.imoveis_vendidos[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_vendidos[0].proprietario |should| equal_to(proprietario)
        administradora_imovel.imoveis_vendidos[0].preco_venda |should| equal_to(60000.00)
        administradora_imovel.imoveis_comprados |should| equal_to([])

    def test_imoveis_monitorados(self):
        endereco = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel( 600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.monitorar_imovel(imovel)
        administradora_imovel.imoveis_monitorados[0] |should| equal_to(imovel)
        
if __name__ == "__main__":
    unittest.main()

