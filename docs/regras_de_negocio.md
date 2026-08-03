# Regras de Negócio

**Projeto:** MOTIX
**Versão:** 1.0
**Sprint:** 0

---

# Pessoa

RN-001 - Toda pessoa deve possuir um CPF.

RN-002 - O CPF é obrigatório (NOT NULL).

RN-003 - O CPF deve ser único no sistema.

RN-004 - O CPF é imutável após o cadastro.

RN-005 - Toda pessoa deve possuir nome.

RN-006 - Toda pessoa deve possuir data de nascimento.

RN-007 - A idade não será armazenada, sendo calculada a partir da data de nascimento.

RN-008 - Telefone é opcional.

RN-009 - E-mail é opcional.

RN-010 - O nome pode ser alterado mediante necessidade.

RN-011 - A data de nascimento não pode ser alterada.

---

# Funcionário

RN-012 - Todo funcionário deve possuir um ID interno.

RN-013 - Todo funcionário deve possuir CPF.

RN-014 - O ID é gerado automaticamente pela concessionária.

RN-015 - Todo funcionário deve possuir um cargo.

RN-016 - Todo funcionário deve possuir um status.

RN-017 - O funcionário não poderá existir sem uma função definida.

---

# Cliente

RN-018 - O endereço será armazenado apenas para clientes.

RN-019 - Um cliente poderá adquirir vários veículos.

---

# Veículo

RN-020 - Todo veículo pertence à concessionária.

RN-021 - Todo veículo possui um status.

RN-022 - O veículo pode estar:

- Disponível
- Reservado
- Vendido

RN-023 - Um veículo vendido não poderá ser vendido novamente.

---

# Concessionária

RN-024 - Apenas a concessionária poderá cadastrar funcionários.

RN-025 - Apenas a concessionária poderá cadastrar veículos.

RN-026 - A concessionária controla clientes, funcionários, veículos e oficina.

---

# Oficina

RN-027 - A oficina recebe apenas veículos.

RN-028 - A oficina identifica posteriormente se o veículo é carro ou moto.