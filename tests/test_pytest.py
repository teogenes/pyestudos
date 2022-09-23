from pytest import fixture, raises, mark
from pytestes.testes.jogo import brincadeira
import sys
import pytest

pytestmark = [
    pytest.mark.stdout,
]


"""
O teste é formado por 3 etapas(GWT - AAA):

- Give - Dado
- When - Quando
- Then - Então

- Arange
- Act
- Assert

Livro xUnit Pattern

- Setup: Onde montamos as coisas - Dado
- Exercise: Onde chamamos as coisas - Quando
- Assert: Onde verificamos as coisas - Então
- TearDown: Onde desmontamos as coisas - Desmonta tudo

"""


def test_quando_bricadeira_receber_1_entao_deve_retornar_1():
    """
    - Bricadeira - SUT - System Under Test
    """
    # Arange
    entrada = 1  # Give
    esperado = 1  # Give
    # Act
    resultado = brincadeira(entrada)  # When
    # Assert
    assert resultado == esperado  # Then


def test_quando_bricadeira_receber_2_entao_deve_retornar_2():
    # Versão pequena
    # TDD Kent beck - One-step test
    assert brincadeira(2) == 2


def test_quando_bricadeira_receber_3_entao_deve_retornar_queijo():
    # One-step test
    assert brincadeira(3) == 'queijo'


@mark.goiabada
def test_quando_bricadeira_receber_5_entao_deve_retornar_goiabada():
    # One-step test
    assert brincadeira(5) == 'goiabada'


def test_quando_bricadeira_receber_10_entao_deve_retornar_goiabada():
    # One-step test
    assert brincadeira(10) == 'goiabada'


@mark.skip(reason='Ainda não implementei')
def test_quando_bricadeira_receber_20_entao_deve_retornar_goiabada():
    # One-step test
    assert brincadeira(20) == 'goiabada'


@mark.skipif(sys.platform == 'linux', reason='pular o teste no linux')
def test_skipif():
    # One-step test
    assert brincadeira(54) == 'goiabada'


@mark.xfail
def test_xfail1():
    # One-step test
    assert brincadeira(20) == 'goiabada'


@mark.xfail
def test_xfail2():
    # One-step test
    assert brincadeira(20) != 'goiabada'


@mark.param
@mark.parametrize('entrada', [5, 10, 15])
def test_bricadeira_deve_retornar_goiabada_multiplos_de_5(entrada):
    # One-step test
    assert brincadeira(entrada) == 'goiabada'


@mark.param
@mark.parametrize('entrada', [3, 6, 9, 12, 18])
def test_bricadeira_deve_retornar_queijo_multiplos_de_3(entrada):
    # One-step test
    assert brincadeira(entrada) == 'queijo'


@mark.param
@mark.parametrize('entrada,esperado', [(1, 1), (2, 2), (3, 'queijo'), (4, 4), (5, 'goiabada')])
def test_bricadeira_deve_retornar_valor_esperado(entrada, esperado):
    # One-step test
    assert brincadeira(entrada) == esperado


@mark.stdout
def test_brincadeira_deve_escrever_msg_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr()
    assert resultado.out == 'Amostra msg no console!\n'


@fixture
def minha_fixture():
    return 3


@mark.stdout
def test_minha_fixture_em_acao(minha_fixture):
    print(minha_fixture)


@mark.stdout
def test_quando_bricadeira_receber_str_entao_deve_retornar_execao():
    # One-step test
    with raises(TypeError):
        brincadeira('3')
