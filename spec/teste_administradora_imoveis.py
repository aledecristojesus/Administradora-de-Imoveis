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
        administradora_imovel.comprar_imovel(imovel, 45000.00, 50000.00)

        administradora_imovel.imoveis_comprados[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_comprados[0].proprietario |should| equal_to("Imortal")
        administradora_imovel.imoveis_comprados[0].antigo_proprietario |should| equal_to(proprietario)
        administradora_imovel.imoveis_comprados[0].preco_compra |should| equal_to(45000.00)
        administradora_imovel.imoveis_comprados[0].preco_minimo_venda |should| equal_to(50000.00)

    def test_registra_venda_de_imovel_e_remove_do_conjunto_de_imoveis_disponiveis(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.comprar_imovel(imovel, 45000.00, 50000.00)
        administradora_imovel.vender_imovel(imovel, proprietario, 60000.00)

        administradora_imovel.imoveis_vendidos[0] |should| equal_to(imovel)
        administradora_imovel.imoveis_vendidos[0].proprietario |should| equal_to(proprietario)
        administradora_imovel.imoveis_vendidos[0].preco_venda |should| equal_to(60000.00)
        administradora_imovel.imoveis_comprados |should| equal_to([])

    def test_nao_registra_venda_de_imovel_se_ele_nao_estiver_disponivel(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        (lambda: administradora_imovel.vender_imovel(imovel, proprietario, 60000.00)) |should| throw(Exception, message = "Imovel nao disponivel para venda.")

    def test_registra_imovel_de_interesse_para_monitoracao(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98", "96260211", endereco)
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)
        administradora_imovel.monitorar_imovel(imovel)

        administradora_imovel.imoveis_monitorados[0] |should| equal_to(imovel)

    #REFATORAR
    def test_emite_relacao_de_imoveis_disponiveis_para_venda(self):
        endereco_1 = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_2 = Endereco("Rua Herculano", 765, "Centro", "Duque de Caxias", "RJ", "28200-000")
        endereco_3 = Endereco("Rua dos Bobos", 0, "Centro", "Duque de Caxias", "RJ", "28200-000")

        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco_1)
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco_1)

        imovel_1 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario, endereco_1)
        imovel_2 = Imovel(500, "2 quartos, 1 sala, 1 banheiros", proprietario, endereco_2)
        imovel_3 = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco_3)

        administradora_imovel.comprar_imovel(imovel_1, 100000.00, 110000.00)
        administradora_imovel.comprar_imovel(imovel_2, 90000.00, 100000.00)
        administradora_imovel.comprar_imovel(imovel_3, 80000.00, 90000.00)

        relatorio_esperado_1 = (endereco_1, 400, "1 quarto, 1 sala, 1 banheiros", proprietario, 110000.00)
        relatorio_esperado_2 = (endereco_2, 500, "2 quartos, 1 sala, 1 banheiros", proprietario, 100000.00)
        relatorio_esperado_3 = (endereco_3, 600, "3 quartos, 1 sala, 2 banheiros", proprietario, 90000.00)

        administradora_imovel.emitir_relacao_de_imoveis_disponiveis() |should| equal_to([relatorio_esperado_1, relatorio_esperado_2, relatorio_esperado_3])

    #REFATORAR
    def test_emite_relacao_de_imoveis_vendidos_por_bairro(self):
        endereco_1 = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_2 = Endereco("Rua Herculano", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_3 = Endereco("Rua dos Bobos", 0, "Jardim das Oliveiras", "Duque de Caxias", "RJ", "28200-000")

        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco_1)

        antigo_proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco_1)
        novo_proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco_1)

        imovel_1 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", antigo_proprietario, endereco_1)
        imovel_2 = Imovel(500, "2 quartos, 1 sala, 1 banheiros", antigo_proprietario, endereco_2)
        imovel_3 = Imovel(600, "3 quartos, 1 sala, 2 banheiros", antigo_proprietario, endereco_3)

        administradora_imovel.comprar_imovel(imovel_1, 100000.00, 110000.00)
        administradora_imovel.comprar_imovel(imovel_2, 90000.00, 100000.00)
        administradora_imovel.comprar_imovel(imovel_3, 80000.00, 90000.00)

        administradora_imovel.vender_imovel(imovel_1, novo_proprietario, 110000.00)
        administradora_imovel.vender_imovel(imovel_2, novo_proprietario, 100000.00)
        administradora_imovel.vender_imovel(imovel_3, novo_proprietario, 90000.00)

        relatorio_esperado_1 = [("Das Pedras", antigo_proprietario, novo_proprietario, 110000.00, 100000.00),
                                ("Das Pedras", antigo_proprietario, novo_proprietario, 100000.00, 90000.00)]
        relatorio_esperado_2 = [("Jardim das Oliveiras", antigo_proprietario, novo_proprietario, 90000.00, 80000.00)]

        administradora_imovel.emitir_relacao_de_imoveis_vendidos_por_bairro() |should| equal_to({"Das Pedras" : relatorio_esperado_1, "Jardim das Oliveiras" : relatorio_esperado_2})

    def test_emite_relacao_de_proprietarios_que_compraram_mais_de_um_imovel(self):
        endereco_1 = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_2 = Endereco("Rua Herculano", 50, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_3 = Endereco("Rua dos Bobos", 100, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")

        proprietario_1 = Proprietario("Astrobaldo Ricks", "123456789-00","2722-2222", endereco_1)
        proprietario_2 = Proprietario("Mr Mini Me", "123456789-01","2722-1111", endereco_2)
        proprietario_3 = Proprietario("Dr Dolittle", "123456789-02","2722-0001", endereco_3)

        imovel_1 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario_3, endereco_1)
        imovel_2 = Imovel(500, "2 quartos, 1 sala, 1 banheiros", proprietario_3, endereco_1)
        imovel_3 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario_3, endereco_1)
        imovel_4 = Imovel(500, "2 quartos, 1 sala, 1 banheiros", proprietario_3, endereco_1)
        imovel_5 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario_3, endereco_1)

        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco_1)
        administradora_imovel.comprar_imovel(imovel_1, 100000.00, 110000.00)
        administradora_imovel.comprar_imovel(imovel_2, 90000.00, 100000.00)
        administradora_imovel.comprar_imovel(imovel_3, 80000.00, 90000.00)
        administradora_imovel.comprar_imovel(imovel_4, 80000.00, 90000.00)
        administradora_imovel.comprar_imovel(imovel_5, 80000.00, 90000.00)

        administradora_imovel.vender_imovel(imovel_1, proprietario_1, 110000.00)
        administradora_imovel.vender_imovel(imovel_2, proprietario_1, 100000.00)
        administradora_imovel.vender_imovel(imovel_3, proprietario_2, 90000.00)
        administradora_imovel.vender_imovel(imovel_4, proprietario_2, 110000.00)
        administradora_imovel.vender_imovel(imovel_5, proprietario_3, 100000.00)

        relatorio_esperado_1 = ("Astrobaldo Ricks", "123456789-00", endereco_1, "2722-2222")
        relatorio_esperado_2 = ("Mr Mini Me", "123456789-01", endereco_2, "2722-1111")

        administradora_imovel.emitir_relacao_de_compradores_recorrentes() |should| equal_to([relatorio_esperado_1, relatorio_esperado_2])

    def test_emite_relacao_de_proprietarios_que_venderam_para_a_imobiliaria_mais_de_um_imovel(self):
        endereco_1 = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_2 = Endereco("Rua Herculano", 50, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco_3 = Endereco("Rua dos Bobos", 100, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")

        proprietario_1 = Proprietario("Astrobaldo Ricks", "123456789-00","2722-2222", endereco_1)
        proprietario_2 = Proprietario("Mr Mini Me", "123456789-01","2722-1111", endereco_2)
        proprietario_3 = Proprietario("Dr Dolittle", "123456789-02","2722-0001", endereco_3)

        imovel_1 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario_1, endereco_1)
        imovel_2 = Imovel(500, "2 quartos, 1 sala, 1 banheiros", proprietario_1, endereco_1)
        imovel_3 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario_2, endereco_1)
        imovel_4 = Imovel(500, "2 quartos, 1 sala, 1 banheiros", proprietario_2, endereco_1)
        imovel_5 = Imovel(400, "1 quarto, 1 sala, 1 banheiros", proprietario_3, endereco_1)

        administradora_imovel = AdministradoraImovel("Imortal", "45635656777", endereco_1)
        administradora_imovel.comprar_imovel(imovel_1, 100000.00, 110000.00)
        administradora_imovel.comprar_imovel(imovel_2, 90000.00, 100000.00)
        administradora_imovel.comprar_imovel(imovel_3, 80000.00, 90000.00)
        administradora_imovel.comprar_imovel(imovel_4, 80000.00, 90000.00)
        administradora_imovel.comprar_imovel(imovel_5, 80000.00, 90000.00)

        relatorio_esperado_1 = ("Astrobaldo Ricks", "2722-2222")
        relatorio_esperado_2 = ("Mr Mini Me", "2722-1111")

        administradora_imovel.emitir_relacao_de_proprietarios_fornecedores_recorrentes() |should| equal_to([relatorio_esperado_1, relatorio_esperado_2])

if __name__ == "__main__":
    unittest.main()
