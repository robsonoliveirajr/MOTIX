import pytest
from datetime import date

from motix.models.pessoa import Pessoa


class PessoaTeste(Pessoa):
    pass


def test_deve_criar_pessoa_com_data_de_nascimento_valida():
    pessoa = PessoaTeste(
        nome="João Silva", cpf="12345678909", data_nascimento=date(2000, 8, 7)
    )

    assert pessoa.data_nascimento == date(2000, 8, 7)


def test_nao_deve_permitir_data_de_nascimento_futura():
    with pytest.raises(ValueError):
        PessoaTeste(
            nome="João Silva",
            cpf="12345678909",
            data_nascimento=date(2030, 8, 7)
        )


def test_deve_calcular_idade_corretamente():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="12345678909",
        data_nascimento=date(2000, 8, 7)
    )

    idade = pessoa.calcular_idade(date(2026, 8, 7))

    assert idade == 26


def test_deve_considerar_aniversario_ainda_nao_ocorrido():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="12345678909",
        data_nascimento=date(2000, 12, 10)
    )

    idade = pessoa.calcular_idade(date(2026, 8, 7))

    assert idade == 25


def test_pessoa_com_18_anos_deve_ser_maior_de_idade():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="12345678909",
        data_nascimento=date(2008, 8, 7)
    )

    assert pessoa.eh_maior_de_idade() is True


def test_pessoa_com_17_anos_nao_deve_ser_maior_de_idade():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="12345678909",
        data_nascimento=date(2008, 12, 10)
    )

    assert pessoa.eh_maior_de_idade() is False
