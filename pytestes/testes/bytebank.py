from datetime import date

class Funcionario:
    
    def __init__(self, nome, data_nascimento, salario) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario


    @property
    def nome(self):
        return self._nome


    @property
    def salario(self):
        return self._salario


    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]


    def idade(self):
  
        data_nascimento_split = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_split[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)


    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('o salario é muito alto para receber um bonus!')
        return valor


    def _eh_socio(self):
        sobrenomes = ['Teogenes','Alves','Assis']
        return (self._salario >= 100_000) and (self.sobrenome() in sobrenomes)


    def decrecimo_salario(self):
        if self._eh_socio():
            decrecimo = self._salario * 0.1
            self._salario = self._salario - decrecimo


    def __str__(self) -> str:
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
