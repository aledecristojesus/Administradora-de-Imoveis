#!/usr/bin/env python
# encoding: utf-8

from spec_helper import *


class TestEndereco(unittest.TestCase):

    def test_inicializa_atributos(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        endereco.rua |should| equal_to("Rua Tatagiba")
        endereco.numero |should| equal_to(765)
        endereco.bairro |should| equal_to("Das Pedras")
        endereco.cidade |should| equal_to("Duque de Caxias")
        endereco.uf |should| equal_to("RJ")
        endereco.cep |should| equal_to("28200-000")

if __name__ == "__main__":
    unittest.main()
