#!/usr/bin/env python
# encoding: utf-8

import unittest
from should_dsl import should
from imovel import Imovel
from proprietario import Proprietario
from endereco import Endereco


class TestImovel(unittest.TestCase):
    
    def test_inicializa_atributos(self):
        endereco_proprietario = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        antigo_proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco_proprietario)
        endereco = Endereco( "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        imovel = Imovel( 600, "3 quartos, 1 sala, 2 banheiros", "50000.00", "45000.00", antigo_proprietario, endereco)
        imovel.area |should| equal_to(600)
        imovel.antigo_proprietario |should| equal_to(antigo_proprietario)
        imovel.proprietario |should| equal_to("Imortal")
        imovel.preco_minimo |should| equal_to("50000.00")
        imovel.descricao |should| equal_to ("3 quartos, 1 sala, 2 banheiros")
if __name__ == "__main__":
    unittest.main()
