# 🤖 ChatBot - Projeto de Wild

Sistema de atendimento ao cliente via terminal desenvolvido em Python, voltado para uma loja de produtos rurais. O chatbot permite gerenciar clientes, realizar pedidos, rastrear compras e emitir relatórios, tudo por meio de menus interativos no console.

---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Gabriel F | [@gabrielfigueired0](https://github.com/gabrielfigueired0) |
| Gabriel K | — |https://github.com/nunesdiego784
| Diego | — |
| Kauan | — |
| João Tosta | — |

---

## 📋 Funcionalidades

- **Cadastro e Suporte**
  - Cadastrar, listar, alterar e excluir clientes
  - Canal de suporte ao cliente

- **Informações**
  - Horários de atendimento
  - Canais de contato
  - Políticas e termos
  - Perguntas frequentes (FAQ)

- **Pedidos**
  - Realizar novo pedido com busca por palavra-chave
  - Rastrear pedidos por CPF
  - Cancelar pedidos ativos
  - Histórico completo de pedidos

- **Relatórios**
  - Relatório geral de clientes e pedidos
  - Relatório individual por cliente (CPF)

---

## 🗂️ Estrutura do Projeto

```
ChatBot-ProjetodeWild/
├── ChatBot/
│   ├── main.py            # Menu principal e submenus
│   ├── clientes.py        # CRUD de clientes
│   ├── ordens_servico.py  # Lógica de pedidos
│   ├── relatorios.py      # Geração de relatórios em .txt
│   ├── persistencia.py    # Leitura e escrita em JSON
│   ├── validacoes.py      # Funções auxiliares de UI
│   └── dados_iniciais.py  # Dados de exemplo e textos informativos
├── dados/
│   ├── clientes.json      # Persistência de clientes
│   └── pedidos.json       # Persistência de pedidos
└── Relatorios/
    └── relatorio_geral.txt
```

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.10 ou superior (necessário para `match/case`).

```bash
# Clone o repositório
git clone https://github.com/gabrielfigueired0/ChatBot-ProjetodeWild.git
cd ChatBot-ProjetodeWild/ChatBot

# Execute o programa
python main.py
```

---

## 💾 Persistência de Dados

Os dados de clientes e pedidos são salvos automaticamente em arquivos `.json` dentro da pasta `dados/` ao encerrar o atendimento. Na próxima execução, os dados são carregados automaticamente. Caso os arquivos não existam, o sistema inicializa com uma massa de dados de exemplo.

---

## 🛠️ Tecnologias

- **Python 3.10+**
- Módulos nativos: `json`, `os`, `datetime`, `unicodedata`
- Estrutura de controle moderna com `match/case`
