# Arquitetura do Projeto

## Hierarquia das Classes

(diagrama)

---

## Relações

Pessoa
│
├── Cliente
│
└── Funcionário
      ├── Vendedor
      └── Mecânico

Veículo
│
├── Carro
└── Moto

Concessionária
│
├── Clientes
├── Funcionários
├── Veículos
└── Oficina

## Pessoa
Classe abstrata responsavel por representar qualquer individuo relacionado ao sistema.

## Funcionario
Classe abstrata que centraliza todas as caracteristicas comuns aos funcionarios da concessionaria.

## Cliente
Especialização de Pessoa responsavel pelos clientes da concessionaria. 

## Veiculo
Classe abstrata que representa qualquer veiculo pertencente ao estoque.

## Concessionaria
Classe principal responsavel por coordenar as entidades do dominio 