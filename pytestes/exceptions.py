"""_summary_"""
import sys
from pprint import pprint


class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    """_summary_"""    
    def __init__(self, message: str = '', saldo: float = None, valor: int = None, *args) -> None:
        self.saldo = saldo
        self.valor = valor
        
        msg = 'Saldo insuficiente para efetuar a transacao\n' \
            f'Saldo atual: {self.saldo} Valor a ser sacado: {self.valor}'
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.saldo, self.valor, *args)


class Cliente:
    
    def __init__(self, nome: str, cpf: int, profissao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

    def __repr__(self) -> str:
        return str(self.__dict__)


cliente  = Cliente('Teogenes',673181343,'Analista')
cliente1 = Cliente('Patricia',673181388,'Gerente')
# Estatico para leitora e dinamico para escrita
cliente.idade = 20

#pprint(cliente.__dict__, width=40)
#print(cliente.idade)



class ContaCorrente:
    
    total_de_contas_criadas = 0
    taxa_operacao = None
    def __init__(self, cliente: Cliente, agencia: int, conta: int) -> None:
        self.__saldo = 100
        self.cliente = cliente
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
        self.__agencia = agencia
        self.conta = conta


        ContaCorrente.total_de_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_de_contas_criadas

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, float):
            raise ValueError("O atributo saldo deve ser um decimal", value)
        
        self.__saldo = value

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, value: int):
        if not isinstance(value, int):
            raise TypeError('O valor deve ser inteiro')
        self.__agencia = value

    def transferencia(self, valor: float, favorecido: object) -> None:
        if valor < 0:
            raise ValueError('O valor a ser sacado não pode ser menos que zero!')
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidas += 1
            E.args = ()
            # para propagar o erro para o traceback
            #raise
            # ou
            #raise E
            # ou
            raise OperacaoFinanceiraError('Operação não finalizada') from E
        favorecido.deposito(valor)
        

    def sacar(self, valor) -> None:
        if valor < 0:
            raise ValueError('O valor a ser sacado não pode ser menos que zero!')
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', self.saldo, valor)
        self.__saldo -= valor

    def deposito(self, valor: float) -> None:
        self.__saldo += valor


conta1 = ContaCorrente(cliente, 123, 4568)
conta2 = ContaCorrente(cliente1, 321, 8574)

vareavel_local_nome = 'conta2'
if vareavel_local_nome in locals():
    print(f'verifica se existe uma vareavel local ({vareavel_local_nome}) no contexto!')
else:
    print('Não existi a vareavel local ({vareavel_local_nome}) no contexto!')

# acessando metodo privado
# pprint(conta1._ContaCorrente__saldo)

try:
    #breakpoint()
    conta1.agencia = '22'
    print('Agencia:', conta1.agencia)
except TypeError as e:
    print(e.args)
    sys.exit()

#-------------------------------------------------

try:
    conta1.deposito(15)
    conta1.sacar(15000)
    pprint(f"Saldo: {conta1.saldo}" )

except OperacaoFinanceiraError as e:
    import traceback
    traceback.print_exc()
    sys.exit()

#-------------------------------------------------

try:

    conta1.transferencia(10000, conta2)
    print('ContaCorrente 1:', conta1.saldo)
    print('ContaCorrente 2:', conta2.saldo)

except OperacaoFinanceiraError as E:
    
    import traceback
    print(E.__context__.saldo) # com a propagação no contesto mante os valores obtido com __context 
    print(E.__context__.valor) # com a propagação no contesto mante os valores obtido com __context
    print('Exeção:', E.__class__.__name__)
    traceback.print_exc()
    sys.exit()