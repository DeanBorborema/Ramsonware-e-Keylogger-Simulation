# 🔐 Simulação de Malware com Python (Ransomware + Keylogger)

## 📌 Descrição do Projeto

Este projeto tem como objetivo demonstrar, em um ambiente **controlado e educacional**, o funcionamento de dois tipos comuns de malware:

* **Ransomware (Simulado)**: criptografia de arquivos e geração de mensagem de resgate
* **Keylogger (Simulado)**: captura de teclas digitadas e armazenamento em arquivo

A proposta é compreender, na prática, como essas ameaças operam, além de estudar **formas de detecção e mitigação**.

> ⚠️ **Aviso**: Este projeto foi desenvolvido exclusivamente para fins educacionais, em ambiente isolado.

---

## 🎯 Objetivos de Aprendizagem

* Entender o funcionamento de ransomware e keyloggers
* Identificar vulnerabilidades exploradas por esses ataques
* Desenvolver scripts em Python simulando cenários reais
* Analisar estratégias de defesa e prevenção
* Documentar experimentos e utilizá-los como portfólio técnico

---

## 🛠️ Tecnologias Utilizadas

* Python 3.13
* Biblioteca `cryptography`
* Biblioteca `pynput`
* Sistema operacional Windows

---

## 🧪 Estrutura do Projeto

```
📁 ransomware-e-keylogger-simulation/
│
├── ransomware.py
├── keylogger.py
├── chave.key
├── LEIA ISSO AGORA.txt
├── logs.txt
└── README.md
```

---

## 🔒 Ransomware Simulado

### ✔️ Funcionalidades

* Geração de chave criptográfica
* Criptografia de arquivos em diretório específico
* Geração de mensagem de resgate
* Possibilidade de descriptografia

### ⚙️ Funcionamento

O script percorre os arquivos do diretório definido e aplica criptografia utilizando o algoritmo Fernet.

### 🧩 Aprendizados

* Importância de ignorar diretórios sensíveis (ex: `.git`)
* Problemas com permissões de arquivos
* Interferência de antivírus ao detectar comportamento suspeito

---

## ⌨️ Keylogger Simulado

### ✔️ Funcionalidades

* Captura de teclas digitadas
* Armazenamento em arquivo `.txt`
* Tratamento de teclas especiais

### ⚙️ Funcionamento

Utiliza a biblioteca `pynput` para escutar eventos de teclado e registrar entradas do usuário.

### 🧩 Aprendizados

* Nem todas as teclas possuem `.char`
* Necessidade de tratamento de exceções
* Possível bloqueio por mecanismos de segurança

---

## 🛡️ Reflexão sobre Defesa e Prevenção

Durante o desenvolvimento, foi possível observar como sistemas modernos implementam mecanismos de proteção:

### 🔹 Antivírus

Detectam:

* Criptografia em massa
* Captura de entrada do usuário
* Acesso suspeito a arquivos

### 🔹 Controle de Acesso

* Restrições de permissão
* Proteção de diretórios críticos

### 🔹 Sandboxing

Execução em ambientes isolados evita impactos reais no sistema.

### 🔹 Conscientização

Usuários são frequentemente o elo mais vulnerável em ataques.

---

## 🧠 Conclusão

Este projeto permitiu compreender, de forma prática, o funcionamento básico de malwares e como eles são detectados.

Reforça a importância de:

* ambientes seguros para testes
* múltiplas camadas de defesa
* boas práticas em segurança da informação

---

## 🚀 Como Executar

> ⚠️ Execute apenas em ambiente controlado

```
pip install cryptography pynput
python ransomware.py
python keylogger.py
```

---

## 📎 Entrega

Este repositório contém:

* Scripts desenvolvidos
* Documentação detalhada
* Simulação prática de ameaças reais

---

## 📷 (Opcional)

Adicionar imagens na pasta `/images` demonstrando:

* Execução dos scripts
* Arquivos antes/depois da criptografia
* Logs gerados

---
