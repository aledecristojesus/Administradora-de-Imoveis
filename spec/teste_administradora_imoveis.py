#!/usr/bin/env python
# encoding: utf-8

from spec_helper import *


class TestAdministradoraImoveis(unittest.TestCase):

    def test_inicializa_atributos(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)

        administradora_imovel.nome |should| equal_to("Imortal")
        administradora_imovel.cnpj |should| equal_to("45635656777")
        administradora_imovel.endereco |should| equal_to(endereco)
        administradora_imovel.imoveis_comprados |should| equal_to([])
        administradora_imovel.imoveis_vendidos |should| equal_to([])
        administradora_imovel.imoveis_monitorados |should| equal_to([])

    def test_registra_compra_de_imovel(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.comprar_imovel(imovel)

        administradora_imovel.imoveis_comprados[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_comprados[0].proprietario |should| equal_to("Imortal")
        administradora_imovel.imoveis_comprados[0].antigo_proprietario |should| equal_to(proprietario)

    def test_registra_venda_de_imovel_e_remove_do_conjunto_de_imoveis_disponiveis(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.comprar_imovel(imovel)
        administradora_imovel.vender_imovel(imovel, proprietario, 60000.00)

        administradora_imovel.imoveis_vendidos[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_vendidos[0].proprietario |should| equal_to(proprietario)
        administradora_imovel.imoveis_vendidos[0].preco_venda |should| equal_to(60000.00)
        administradora_imovel.imoveis_comprados |should| equal_to([])

    def test_registra_imovel_de_interesse_para_monitoracao(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98", "96260211", endereco)
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.monitorar_imovel(imovel)

        administradora_imovel.imoveis_monitorados[0] |should| equal_to(imovel)

if __name__ == "__main__":
    unittest.main()
