# ♻️ EcoData - Sistema de Cadastro de Lixeiras

O **EcoData** é um sistema de gerenciamento de lixeiras inteligentes, desenvolvido em Python.  
Ele permite **cadastrar, listar, atualizar e deletar** informações sobre lixeiras, ajudando no controle e monitoramento.

---

## 📂 Funcionalidades

- **Inserir**: Cadastra uma nova lixeira com:
  - Número de Série
  - Endereço
  - Situação (Ativa/Inativa/Cheia/Em Manutenção)
  - Data de Instalação
  - Capacidade (litros)

- **Listar**: Exibe todas as lixeiras cadastradas em formato de tabela.

- **Atualizar**: Permite alterar qualquer informação de uma lixeira existente.

- **Deletar**:
  - Remover toda a lixeira.
  - Remover campos específicos (endereço, situação, data de instalação ou capacidade).

---

## 🚀 Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/seurepositorio.git
```

2. Acesse o diretório:
```bash
cd seurepositorio
```

3. Execute o script Python:
```bash
python ecodata.py
```

> É necessário instalar a biblioteca **tabulate**:
```bash
pip install tabulate
```

---

## 📌 Exemplo de Menu

```
======================================
      ♻️ CADASTRO DE LIXEIRAS
======================================

Seja bem vindo ao menu de cadastro
Selecione a opção desejada:

[1] Inserir
[2] Listar
[3] Atualizar
[4] Deletar
```

---

## 🎯 Objetivo

O objetivo do **EcoData** é fornecer uma solução simples e interativa para o **gerenciamento de lixeiras urbanas**,  
permitindo fácil controle das condições e localizações.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** – sinta-se livre para usar, modificar e compartilhar.
