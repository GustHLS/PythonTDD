import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from codigo.bytebank import Funcionario
from pytest import mark

class TestClass:

    def test_retorna_nome(self):
        entrada = 'Gustavo Henrique'
        esperado = 'Gustavo Henrique'
        gustavo = Funcionario(entrada, '11/11/2000', 1111)
        resultado = gustavo.nome

        assert resultado == esperado

    def test_retorna_se_eh_socio(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = True

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        resultado = funcionario_teste._eh_socio()

        assert resultado == esperado

    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 25

        # When-Ação
        Funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = Funcionario_teste.idade()

        # Then-Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Gustavo_Henrique_deve_retornar_Henrique(self):
        entrada = 'Gustavo Henrique'
        esperado = 'Henrique'

        gustavo = Funcionario(entrada, '11/11/2000', 1111)
        resultado = gustavo.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000
            
            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
