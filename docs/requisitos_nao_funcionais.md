# Requisitos Não Funcionais 

**Projeto:** MOTIX
**Versão:** 1.0
**Data:** 21/07/2026
**Autor:** Robson de Oliveira Junior
**Sprint:** 0

---

# Introdução

Este documento descreve os requisitos não funcionais do sistema MOTIX.

Os requisitos não funcionais estabelecem padrões técnicos e de qualidade que deverão ser seguidos durante todo o desenvolvimento do projeto.

---

# RNF-001 – Linguagem

O sistema deverá ser desenvolvido utilizando Python 3.12 ou superior.

---

# RNF-002 – Paradigma

O projeto deverá utilizar Programação Orientada a Objetos (POO).

---

# RNF-003 – Arquitetura

O código deverá ser organizado de forma modular, separando responsabilidades em diferentes pacotes e módulos.

---

# RNF-004 – Padrão de Código

O código deverá seguir, sempre que possível, as recomendações da PEP 8.

---

# RNF-005 – Princípios SOLID

O projeto deverá aplicar os princípios SOLID sempre que possível, visando facilitar manutenção, reutilização e escalabilidade.

---

# RNF-006 – Versionamento

Todo o desenvolvimento deverá ser versionado utilizando Git e hospedado no GitHub.

Cada funcionalidade deverá ser registrada por meio de commits descritivos.

---

# RNF-007 – Documentação

Toda decisão importante deverá ser documentada na pasta docs.

O projeto deverá possuir documentação suficiente para facilitar sua compreensão e manutenção.

---

# RNF-008 – Testes

As funcionalidades implementadas deverão possuir testes automatizados utilizando Pytest.

---

# RNF-009 – Banco de Dados

A persistência de dados será implementada utilizando SQLite na primeira versão com banco de dados.

A arquitetura deverá permitir a substituição futura por outro SGBD sem grandes alterações.

---

# RNF-010 – API

O sistema deverá ser preparado para disponibilizar uma API REST utilizando FastAPI em versões futuras.

---

# RNF-011 – Escalabilidade

A arquitetura deverá permitir a adição de novas funcionalidades sem necessidade de grandes modificações nas classes existentes.

---

# RNF-012 – Legibilidade

O código deverá priorizar nomes claros para classes, métodos, atributos e variáveis, favorecendo a leitura e manutenção.

---

# RNF-013 – Organização

As classes deverão ser separadas por responsabilidade, evitando arquivos excessivamente grandes ou com múltiplas responsabilidades.

---

# RNF-014 – Portabilidade

O sistema deverá funcionar em qualquer sistema operacional compatível com Python.

---

# RNF-015 – Projeto Educacional

O desenvolvimento do MOTIX terá caráter educacional.

As decisões de arquitetura, modelagem e implementação serão registradas durante toda a evolução do projeto, permitindo acompanhar o processo de construção do software.

---

## RNF-016 – Evolução Incremental

O projeto será desenvolvido em Sprints.

Cada Sprint deverá possuir objetivos definidos, documentação correspondente e registro das principais decisões tomadas durante o desenvolvimento.