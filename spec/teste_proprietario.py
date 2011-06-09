#!/usr/bin/env python
# encoding: utf-8

import unittest
from should_dsl import should
from proprietario import Proprietario

class TestPropritario(unittest.TestCase):

    def test_atributos(self):
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98", "Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000", "96260211")
        proprietario.nome |should| equal_to("Astrobaldo Ricks")
        proprietario.cpf |should| equal_to("987654321-98")
        proprietario.rua |should| equal_to("Rua Tatagiba")
        proprietario.numero |should| equal_to(765)
        proprietario.bairro |should| equal_to("Das Pedras")
        proprietario.cidade |should| equal_to("Duque de Caxias")
        proprietario.uf |should| equal_to("RJ")
        proprietario.cep |should| equal_to("28200-000")
        proprietario.telefone |should| equal_to("96260211")

if __name__=="__main__":
    unittest.main()

