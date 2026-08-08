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
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email

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
