# 🏦 Sistema Bancário em Python — Versão 2.0

Projeto desenvolvido como parte da **Formação Python Developer da DIO**, com o objetivo de aprimorar o sistema bancário criado anteriormente e aplicar novos conceitos de programação em Python.

Esta versão representa uma evolução do primeiro projeto, adicionando novas funcionalidades, organização do código e suporte a múltiplos usuários e contas.

---

## 🚀 Sobre o projeto

O projeto simula algumas das principais operações de um sistema bancário utilizando Python.

Na primeira versão, o sistema permitia realizar operações básicas como depósitos, saques e consulta de extrato.

Nesta nova versão, o sistema foi expandido para permitir o gerenciamento de diferentes usuários e contas, além da realização de transferências entre eles.

O objetivo foi colocar em prática conceitos como:

* Funções
* Estruturas condicionais
* Estruturas de repetição
* Listas
* Dicionários
* Manipulação de dados
* Validação de entradas
* Organização e reutilização de código

---

## ✨ Funcionalidades

O sistema possui as seguintes funcionalidades:

### 👤 Cadastro de usuários e contas

É possível criar diferentes usuários no sistema.

Cada usuário recebe automaticamente:

* Número de conta único
* Saldo individual
* Histórico de depósitos
* Histórico de saques
* Histórico de transferências

O sistema também impede a criação de dois usuários com o mesmo nome.

---

### 💰 Depósitos

Permite realizar depósitos na conta de um usuário.

O sistema:

* Valida valores positivos;
* Atualiza automaticamente o saldo;
* Registra o depósito no histórico da conta.

---

### 💸 Saques

Permite realizar saques respeitando as regras definidas pelo sistema.

Regras:

* Máximo de **3 saques**;
* Limite de **R$ 500,00 por saque**;
* O valor não pode ser maior que o saldo disponível;
* Não são permitidos valores negativos ou iguais a zero.

---

### 🔄 Transferências

Permite transferir valores entre usuários cadastrados.

O sistema verifica:

* Se a conta de destino existe;
* Se o usuário possui saldo suficiente;
* Se o valor informado é válido;
* Se o usuário está tentando transferir para a própria conta.

Ao realizar a transferência:

* O valor é descontado da conta de origem;
* O valor é adicionado à conta de destino;
* A movimentação é registrada nas duas contas.

---

### 📄 Extrato

Cada usuário possui seu próprio extrato bancário.

O extrato apresenta:

* Depósitos realizados;
* Saques realizados;
* Transferências enviadas;
* Transferências recebidas;
* Saldo atual da conta.

---

### 📋 Listagem de contas

O sistema também permite visualizar todas as contas cadastradas, exibindo informações como:

* Nome do usuário;
* Número da conta;
* Saldo atual.

---

## 🔄 Evolução em relação ao primeiro projeto

Este projeto foi desenvolvido como uma evolução da primeira versão do Sistema Bancário em Python.

### Versão 1

A primeira versão possuía:

* Depósito;
* Saque;
* Extrato;
* Controle de saldo;
* Limite de três saques;
* Limite de R$ 500,00 por saque.

### Versão 2

Nesta versão foram adicionados:

* Cadastro de múltiplos usuários;
* Criação automática de contas;
* Número único para cada conta;
* Saldo individual por usuário;
* Histórico individual de movimentações;
* Transferências entre contas;
* Registro de transferências enviadas e recebidas;
* Validação da conta de destino;
* Validação de transferência para a própria conta;
* Listagem das contas cadastradas;
* Melhor organização do código utilizando funções e dicionários.

---

## 🧠 Conceitos praticados

Durante o desenvolvimento do projeto foram utilizados conceitos importantes da linguagem Python, como:

```python
def
if / elif / else
while
for
try / except
listas
dicionários
funções
variáveis globais
f-strings
```

Além disso, o projeto ajudou a praticar lógica de programação, validação de dados e organização de um programa com diferentes funcionalidades.

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Git
* GitHub

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Sugaharaa/Sistema-Bancario-Python-V2-DIO.git
```

### 2. Entre na pasta do projeto

```bash
cd Sistema-Bancario-Python-V2-DIO
```

### 3. Execute o programa

```bash
python SistemaBancario.py
```

---

## 🖥️ Menu do sistema

Ao executar o programa, será exibido o seguinte menu:

```text
========== SISTEMA BANCÁRIO ==========
1. Criar usuário e conta
2. Depositar
3. Sacar
4. Extrato
5. Listar contas
6. Transferir
7. Sair
======================================
```

O usuário pode selecionar uma das opções digitando o número correspondente.

---

## 📁 Estrutura do projeto

```text
Sistema-Bancario-Python-V2-DIO/
│
├── SistemaBancario.py
└── README.md
```

---

## 📈 Aprendizados

Este projeto permitiu evoluir uma aplicação simples para um sistema capaz de trabalhar com diferentes usuários e movimentações bancárias.

Além da implementação das funcionalidades, o desafio ajudou a reforçar conceitos de lógica de programação e mostrou como estruturas como **funções e dicionários** podem ser utilizadas para organizar melhor os dados e tornar o código mais escalável.

O desenvolvimento também reforçou a importância de validar diferentes situações antes de realizar uma operação, como saldo insuficiente, valores inválidos e contas inexistentes.

---

## 🔗 Projeto anterior

Este projeto é uma evolução do primeiro Sistema Bancário desenvolvido durante a Formação Python Developer da DIO.

👉 [Acessar a primeira versão do projeto](https://github.com/Sugaharaa/Projeto-DIO-Python-BackEnd-)

---

## 🎯 Possíveis melhorias futuras

Algumas funcionalidades que podem ser adicionadas futuramente:

* Autenticação de usuários;
* Uso de CPF no cadastro;
* Agência bancária;
* Persistência dos dados em arquivos;
* Banco de dados;
* Interface gráfica;
* Histórico completo das movimentações em ordem cronológica;
* Data e horário das transações;
* Organização do projeto utilizando Programação Orientada a Objetos.

---

## 👩‍💻 Autor

Desenvolvido por **Sugaharaa** durante a **Formação Python Developer da DIO**.

Projeto criado para fins de estudo, prática de Python e construção de portfólio no GitHub. 🚀
