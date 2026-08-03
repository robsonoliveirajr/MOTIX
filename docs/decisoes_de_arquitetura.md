# Decisões de Arquitetura

Este documento registra as principais decisões tomadas durante o desenvolvimento do MOTIX.

---

## DA-001 - Hierarquia de Pessoas

### Decisão

Criar uma superclasse abstrata chamada `Pessoa`.

### Motivação

Clientes e funcionários compartilham diversas características, como:

- nome
- CPF
- data de nascimento
- telefone
- e-mail

Centralizar essas informações evita duplicação de código e facilita futuras manutenções.

---

## DA-002 - CPF imutável

### Decisão

O CPF será:

- obrigatório;
- único;
- imutável.

### Motivação

O CPF representa a identidade da pessoa e não pode ser alterado após o cadastro.

---

## DA-003 - Classe Funcionário

### Decisão

A classe `Funcionario` será abstrata.

### Motivação

Ela representa características comuns aos cargos existentes.

As especializações iniciais serão:

- Mecânico
- Vendedor

---

## DA-004 - Modelagem de cargos

### Decisão

Nesta versão os cargos serão representados por herança.

Pessoa
    ↓
Funcionario
    ↓
Mecânico
Vendedor

### Motivação

A modelagem por herança torna o domínio mais simples e facilita o aprendizado dos conceitos de Programação Orientada a Objetos.

### Evolução futura

Caso o sistema passe a possuir autenticação, perfis de acesso e permissões, essa modelagem poderá evoluir para um sistema baseado em Cargos e Permissões.


## DA-005 - Especialização de Funcionários

### Decisão

A classe `Funcionario` será especializada em subclasses (`Vendedor` e `Mecânico`), cada uma contendo atributos e comportamentos específicos do seu domínio.

### Motivação

Embora ambos sejam funcionários, suas responsabilidades e regras de negócio são distintas. A separação favorece a organização do código, a aplicação do princípio da Responsabilidade Única (SRP) e facilita futuras evoluções do sistema, como implementação de metas, comissões, especialidades técnicas e indicadores de desempenho.

### Evolução futura

Novos cargos poderão ser adicionados como subclasses ou, caso o sistema evolua para um controle mais complexo de usuários e permissões, a modelagem poderá ser revisada para um modelo baseado em cargos e permissões.

## DA-006 - Classe Veículo

### Decisão

Foi criada uma superclasse abstrata chamada `Veiculo`.

### Motivação

A classe representa qualquer veículo comercializado pela concessionária, evitando que a arquitetura fique limitada apenas a carros e motos.

### Escopo atual

Na versão 1.0 do MOTIX serão implementadas apenas as subclasses:

- Carro
- Moto

### Evolução futura

Caso o domínio do sistema seja ampliado para outros segmentos (como caminhões, jet skis ou máquinas agrícolas), novas subclasses poderão ser adicionadas sem necessidade de modificar a classe `Veiculo`.