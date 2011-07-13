#!/usr/bin/env python
# encoding: utf-8

import unittest
from should_dsl import should
from proprietario import Proprietario
from endereco import Endereco


class TestProprietario(unittest.TestCase):

    def test_inicializa_atributos(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras","Duque de Caxias", "RJ", "28200-000")
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98","96260211", endereco)
        proprietario.nome |should| equal_to("Astrobaldo Ricks")
        proprietario.cpf |should| equal_to("987654321-98")
        proprietario.telefone |should| equal_to("96260211")
        proprietario.endereco.rua |should| equal_to("Rua Tatagiba")
        proprietario.endereco.numero |should| equal_to(765)
        proprietario.endereco.bairro |should| equal_to("Das Pedras")
        proprietario.endereco.cidade |should| equal_to("Duque de Caxias")
        proprietario.endereco.uf |should| equal_to("RJ")
        proprietario.endereco.cep |should| equal_to("28200-000")


if __name__ == "__main__":
    unittest.main()
