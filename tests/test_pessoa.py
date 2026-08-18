import pytest
from datetime import date

from motix.models.pessoa import Pessoa


class PessoaTeste(Pessoa):
    pass


def test_deve_criar_pessoa_com_data_de_nascimento_valida():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="12345678909",
        data_nascimento=date(2000, 8, 7)
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


def test_deve_aceitar_cpf_valido():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="52998224725",  # CPF válido
        data_nascimento=date(2000, 8, 7),
    )

    assert pessoa.cpf == "52998224725"


def test_deve_normalizar_cpf_com_mascara():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="529.982.247-25",  # CPF com máscara
        data_nascimento=date(2000, 8, 7),
    )

    assert pessoa.cpf == "52998224725"  # CPF deve ser normalizado sem máscara


def test_não_deve_aceitar_cpf_invalido():
    with pytest.raises(ValueError):
        PessoaTeste(
            nome="João Silva",
            cpf="12345678900",  # CPF inválido
            data_nascimento=date(2000, 8, 7),
        )


def test_nao_deve_aceitar_cpf_com_digitos_repetidos():
    with pytest.raises(ValueError):
        PessoaTeste(
            nome="João Silva",
            cpf="11111111111",  # CPF com dígitos repetidos
            data_nascimento=date(2000, 8, 7),
        )


def test_cpf_nao_deve_ser_alterado():
    pessoa = PessoaTeste(
        nome="João Silva",
        cpf="52998224725",  # CPF válido
        data_nascimento=date(2000, 8, 7),
    )

    with pytest.raises(AttributeError):
        pessoa.cpf = "98765432100"  # Tentativa de alterar o CPF
