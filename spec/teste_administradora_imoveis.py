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

    def test_comprar_imovel(self):
        endereco = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel( 600, "3 quartos, 1 sala, 2 banheiros", "50000.00", "45000.00", proprietario, endereco)
        administradora_imovel.comprar_imovel(imovel)
        administradora_imovel.imoveis_comprados[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_comprados[0].proprietario |should| equal_to("Imortal")
        administradora_imovel.imoveis_comprados[0].antigo_proprietario |should| equal_to(proprietario)


if __name__ == "__main__":
    unittest.main()

