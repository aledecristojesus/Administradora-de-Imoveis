Administradora de Imóveis
=========================

|  Exercício para a prática de conceitos de TDD.
|
|  Instituto Federal Fluminense
|  Bacharelado em Sistemas de Informação
|  Laboratório Orientado a Objetos
|  Professor: Fábio Duncan
|  Alunos: Alexandre Piccinini e Natanael Araújo

Mini-Mundo:
-----------

A administradora de Imóveis "IMOR Tal" é uma empresa que cuida, principalmente, da compra e venda de imóveis residenciais e comerciais no Grande Rio, dentre outras atividades.

O atendimento atualmente e demorado e, muitas vezes, incompleto devido a demora no manuseio de muitas fichas, acarretando a perda de muitas oportunidades de negócio. Todos os imóveis são comprados pela imobiliária para, então, serem colocados a venda. A direção da empresa definiu como prioridade automatizar o processo de comercialização (compra e venda) dos imóveis, envolvendo seus proprietários (novos e antigos). A imobiliária considera "proprietário" toda pessoa que participou de um processo de comercialização (compra ou venda) no papel de dono (antigo ou novo).

Entre outras informações, o sistema deverá ser capaz de controlar os imóveis comprados, vendidos e os de seu “interesse” (não foram comercializados), e emitir:

1.  Relação de todos os imóveis disponíveis para venda, contendo para cada um: Endereço, Bairro, Área (m2), descrição, Proprietário antigo (o atual é a administradora) e o Preço Mínimo para venda
2.  Relação de todos os imóveis vendidos, por bairro, contendo para cada um: Bairro, Proprietário antigo, Proprietário novo, Preço de venda (ao proprietário novo) e o Preço de compra (pela imobiliária)
3.  Relação dos proprietários que compraram mais de um imóvel na imobiliária (nome, CPF, endereço, telefone)
4.  Relação dos proprietários que venderam mais de um imóvel para a imobiliária (nome, telefone)

Testando
--------

Nós usamos `should_dsl <https://github.com/hugobr/should-dsl>`_ para escrever nossos testes. Recomendamos também o uso do `specloud <https://github.com/hugobr/specloud>`_ para uma saída mais amigável. Execute::

  $ specloud spec/
