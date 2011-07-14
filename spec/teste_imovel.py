#!/usr/bin/env python
# encoding: utf-8

from spec_helper import *


class TestImovel(unittest.TestCase):

    def test_inicializa_atributos(self):
        endereco_proprietario = Endereco("Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco_proprietario)
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        imovel = Imovel(600, "3 quartos, 1 sala, 2 banheiros", proprietario, endereco)

        imovel.area |should| equal_to(600)
        imovel.antigo_proprietario |should| equal_to(None)
        imovel.proprietario |should| be(proprietario)
        imovel.endereco |should| be(endereco)
        imovel.preco_minimo_venda |should| equal_to(None)
        imovel.preco_compra |should| equal_to(None)
        imovel.preco_venda |should| equal_to(None)
        imovel.descricao |should| equal_to ("3 quartos, 1 sala, 2 banheiros")

if __name__ == "__main__":
    unittest.main()
