from pytestes.testes.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retorna_22(self):

        #? Given - Contexto
        entrada = '13/03/2000'
        esperado = 22

        func_test = Funcionario('Teste', entrada, 1111)

        #? When - Ação
        resultado = func_test.idade()

        #? Then - Desfecho
        assert resultado == esperado


    def test_quando_sobrenome_recebe_jose_teogenes_deve_retorna_teogenes(self):

        #? Given - Contexto
        entrada = 'jose teogenes'
        esperado = 'teogenes'

        func_test = Funcionario(entrada, '06/09/1986', 1111)

        #? When - Ação
        resultado = func_test.sobrenome()

        #? Then - Desfecho
        assert resultado == esperado


    def test_quando_decrecimo_salario_recebe_1000000_deve_retorna_90000(self):

        #? Given - Contexto
        entrada = 100_000
        esperado = 90_000

        func_test = Funcionario('Jose Teogenes', '06/09/1986', entrada)

        #? When - Ação
        func_test.decrecimo_salario()
        resultado = func_test.salario

        #? Then - Desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retorna_100(self):

        #? Given - Contexto
        entrada = 1_000
        esperado = 100

        func_test = Funcionario('Jose Teogenes', '06/09/1986', entrada)

        #? When - Ação
        resultado = func_test.calcular_bonus()

        #? Then - Desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000000_deve_retorna_exception(self):

        with pytest.raises(Exception):
            #? Given - Contexto
            entrada = 1_000_000_0000

            func_test = Funcionario('Jose Teogenes', '06/09/1986', entrada)

            #? When - Ação
            resultado = func_test.calcular_bonus()

            #? Then - Desfecho
            assert resultado
