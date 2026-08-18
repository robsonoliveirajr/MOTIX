from abc import ABC
from datetime import date


class Pessoa(ABC):

    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: date,
        telefone: str | None = None,
        email: str | None = None,
    ):

        if data_nascimento > date.today():
            raise ValueError("A data de nascimento não pode ser futura.")

        self.nome = nome
        cpf_normalizado = self._normalizar_cpf(cpf)

        if not self._cpf_valido(cpf_normalizado):
            raise ValueError("CPF inválido.")

        self._cpf = cpf_normalizado
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email

    @property
    def cpf(self) -> str:
        return self._cpf

    def calcular_idade(self, data_referencia: date | None = None) -> int:
        hoje = data_referencia or date.today()

        idade = hoje.year - self.data_nascimento.year

        if (hoje.month, hoje.day) < (
            self.data_nascimento.month,
            self.data_nascimento.day,
        ):
            idade -= 1

        return idade

    def eh_maior_de_idade(self) -> bool:
        return self.calcular_idade() >= 18

    def _normalizar_cpf(self, cpf: str) -> str:
        return cpf.replace(".", "").replace("-", "")

    def _cpf_tem_digitos_repetidos(self, cpf: str) -> bool:
        return len(set(cpf)) == 1

    def _cpf_valido(self, cpf: str) -> bool:
        if len(cpf) != 11:
            return False

        if self._cpf_tem_digitos_repetidos(cpf):
            return False

        soma = 0

        for indice in range(9):
            soma += int(cpf[indice]) * (10 - indice)

        resto = soma % 11

        primeiro_digito = 0 if resto < 2 else 11 - resto

        if primeiro_digito != int(cpf[9]):
            return False

        soma = 0

        for indice in range(10):
            soma += int(cpf[indice]) * (11 - indice)

        resto = soma % 11

        segundo_digito = 0 if resto < 2 else 11 - resto

        return segundo_digito == int(cpf[10])
