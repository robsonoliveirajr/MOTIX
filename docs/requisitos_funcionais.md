# Requisitos Funcionais

**Projeto:** MOTIX  
**Versão:** 1.0  
**Data:** 20/07/2026  
**Autor:** Robson de Oliveira Júnior  
**Sprint:** 0

---

# Introdução

Este documento descreve os requisitos funcionais da versão 1.0 do sistema MOTIX.

Cada requisito recebe um identificador único (RF-XXX), permitindo rastrear sua implementação durante o desenvolvimento do projeto.

---

# RF-001 – Cadastro de Clientes

O sistema deve permitir cadastrar um cliente contendo, no mínimo:

- Nome
- Idade
- CPF
- E-mail
- Endereço

---

# RF-002 – Consulta de Clientes

O sistema deve permitir consultar os clientes cadastrados.

---

# RF-003 – Atualização de Clientes

O sistema deve permitir atualizar os dados de um cliente.

---

# RF-004 – Remoção de Clientes

O sistema deve permitir remover um cliente.

---

# RF-005 – Cadastro de Vendedores

O sistema deve permitir cadastrar vendedores contendo:

- Nome
- Idade
- ID
- Quantidade de vendas

---

# RF-006 – Cadastro de Mecânicos

O sistema deve permitir cadastrar mecânicos contendo:

- Nome
- Idade
- ID
- Cargo

---

# RF-007 – Consulta de Funcionários

O sistema deve permitir listar todos os funcionários cadastrados.

---

# RF-008 – Cadastro de Carros

O sistema deve permitir cadastrar carros contendo:

- Fabricante
- Modelo
- Ano
- Quilometragem
- Motorização
- Valor

---

# RF-009 – Cadastro de Motos

O sistema deve permitir cadastrar motocicletas contendo:

- Fabricante
- Modelo
- Ano
- Quilometragem
- Cilindradas
- Valor

---

# RF-010 – Consulta de Veículos

O sistema deve permitir listar todos os veículos cadastrados.

---

# RF-011 – Atualização de Veículos

O sistema deve permitir alterar os dados de um veículo.

---

# RF-012 – Remoção de Veículos

O sistema deve permitir remover um veículo.

---

# RF-013 – Controle de Estoque

O sistema deve manter atualizado o estoque de veículos disponíveis na concessionária.

---

# RF-014 – Cadastro de Funcionários pela Concessionária

Somente a classe Concessionária poderá cadastrar funcionários no sistema.

---

# RF-015 – Associação de Cliente ao Veículo

O sistema deve registrar qual cliente adquiriu determinado veículo.

---

# RF-016 – Associação de Veículos à Concessionária

Todo veículo cadastrado deverá pertencer ao estoque de uma concessionária.

---

# RF-017 – Controle de Quantidade

A concessionária deverá controlar automaticamente:

- Quantidade de clientes;
- Quantidade de funcionários;
- Quantidade de carros;
- Quantidade de motos.

---

# Requisitos futuros

Os requisitos abaixo pertencem às próximas versões do sistema:

- Gerenciamento da Oficina;
- Ordem de Serviço;
- Histórico de Manutenções;
- Banco de Dados;
- API REST;
- Relatórios;
- Interface Gráfica.