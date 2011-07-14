#!/usr/bin/env python
# encoding: utf-8

from spec_helper import *


class TestProprietario(unittest.TestCase):

    def test_inicializa_atributos(self):
        endereco = Endereco("Rua Tatagiba", 765, "Das Pedras", "Duque de Caxias", "RJ", "28200-000")
        proprietario = Proprietario("Astrobaldo Ricks", "987654321-98", "96260211", endereco)

        proprietario.nome |should| equal_to("Astrobaldo Ricks")
        proprietario.cpf |should| equal_to("987654321-98")
        proprietario.telefone |should| equal_to("96260211")
        proprietario.endereco |should| be(endereco)

if __name__ == "__main__":
    unittest.main()
