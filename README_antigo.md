# GeoAI Mentor 🌍🤖

Chatbot assistente especializado para geocientistas que desejam migrar para Ciência de Dados e Inteligência Artificial.

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Chave de API do Google Gemini

## 🚀 Instalação

1. Clone ou baixe este repositório

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

   - Windows: `.\venv\Scripts\Activate.ps1`
   - Linux/Mac: `source venv/bin/activate`

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Configure sua chave de API:
   - Obtenha sua chave em: https://aistudio.google.com/app/apikey
   - Edite o arquivo `.env` e adicione sua chave:
   ```
   GOOGLE_API_KEY="sua_chave_aqui"
   ```

## ▶️ Como Usar

Execute o chatbot:

```bash
python chatbot_mentor.py
```

## 🎯 Funcionalidades

- **Etapa #1**: Chatbot básico sem memória, responde perguntas sequenciais sobre transição de carreira para área de dados

## 📝 Estrutura do Projeto

```
MyGeoAI_Mentor/
├── .env                    # Configuração da API key
├── chatbot_mentor.py       # Código principal do chatbot
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 🤝 Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio para criar um mentor de carreira especializado em ajudar geocientistas (Geofísica, Geologia) a migrarem para a área de Ciência de Dados e IA.
