#!/usr/bin/env python
# encoding: utf-8

import unittest
from should_dsl import should
from imobiliaria import Imovel

class TestImoveis(unittest.TestCase):

    def test_inicializar_atributos(self):
        imovel = Imovel("Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000", "casa", 600)
        imovel.rua |should| equal_to("Rua Tatagiba")
        imovel.numero |should| equal_to(765)
        imovel.bairro |should| equal_to("Das Pedras")
        imovel.cidade |should| equal_to("Duque de Caxias")
        imovel.uf |should| equal_to("RJ")
        imovel.cep |should| equal_to("28200-000")
        imovel.descricao |should| equal_to("casa")
        imovel.area |should| equal_to(600)
        imovel.antigo_proprietario |should| equal_to(None)
        imovel.proprietario |should| equal_to("Imortal")
        imovel.preco_compra |should| equal_to(None)
        imovel.preco_minimo |should| equal_to(None)
        imovel.preco_venda |should| equal_to(None)

if __name__=="__main__":
    unittest.main()

