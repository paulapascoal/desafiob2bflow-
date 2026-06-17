# 🚀 Desafio Técnico — b2bflow

Projeto desenvolvido em Python com o objetivo de integrar o Supabase e a Z-API para automatizar o envio de mensagens via WhatsApp.

## 📋 Sobre o Projeto

A aplicação realiza a leitura de contatos armazenados em uma tabela no Supabase e envia mensagens personalizadas para cada contato utilizando a API da Z-API.

### Fluxo da aplicação

```text
Supabase → Consulta de contatos
         ↓
       Python
         ↓
      Z-API
         ↓
     WhatsApp
```

## 🛠️ Tecnologias Utilizadas

* Python 3.11
* Supabase
* Z-API
* Requests
* Python Dotenv

## 📂 Estrutura do Projeto

```text
.
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=seu_supabase_url
SUPABASE_KEY=sua_supabase_key

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
```

## ▶️ Instalação

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 🚀 Execução

Execute a aplicação:

```bash
python app.py
```

## 📱 Funcionalidades

* Consulta automática de contatos no Supabase
* Personalização da mensagem com o nome do contato
* Envio automatizado de mensagens via WhatsApp
* Utilização de variáveis de ambiente para proteção de credenciais

## 💡 Exemplo de Mensagem

```text
Olá, [pessoa] tudo bem com você?
```

## 👩‍💻 Desenvolvido por

Paula Pascoal

Desafio Técnico — b2bflow
