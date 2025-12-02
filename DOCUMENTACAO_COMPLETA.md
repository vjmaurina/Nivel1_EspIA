# 📚 Documentação Completa - GeoAI Mentor

## 🎯 Objetivo do Projeto

Desenvolver o "GeoAI Mentor", um chatbot assistente especializado que atua como mentor de carreira para geocientistas (geofísicos e geólogos) que desejam migrar para a área de Ciência de Dados e Inteligência Artificial. O diferencial é sua capacidade de manter o contexto da conversa, lembrando de perguntas e respostas anteriores para fornecer aconselhamento coeso e personalizado.

---

## 📦 Tecnologias Utilizadas

- **Python 3.7+**
- **Google Gemini AI** (modelo: gemini-2.0-flash)
- **LangChain** - Framework para desenvolvimento de aplicações com LLMs
- **python-dotenv** - Gerenciamento de variáveis de ambiente

---

## 🚀 Evolução do Projeto

### **Etapa #1: Conexão Básica com a API do Gemini**

#### 🎯 Objetivo

Estabelecer a conexão com a API do Google Gemini e obter respostas simples do modelo de linguagem, sem qualquer tipo de memória ou personalização.

#### 📝 Requisitos Implementados

1. ✅ Importação de bibliotecas (`os`, `dotenv`, `ChatGoogleGenerativeAI`)
2. ✅ Carregamento de variáveis de ambiente do arquivo `.env`
3. ✅ Instanciação do modelo Gemini com `gemini-2.0-flash` e `temperature=0.7`
4. ✅ Criação de lista com duas perguntas sequenciais
5. ✅ Loop para enviar perguntas e imprimir respostas

#### 💻 Código da Etapa #1

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Instancia o modelo Gemini
modelo = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# Lista de perguntas sequenciais
perguntas = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
]

# Loop que envia cada pergunta para o modelo e imprime a resposta
for pergunta in perguntas:
    print(f"\n🔵 Pergunta: {pergunta}")
    resposta = modelo.invoke(pergunta)
    print(f"\n🤖 Resposta: {resposta.content}")
    print("-" * 80)
```

#### 📊 Resultado da Etapa #1

- ✅ Conexão bem-sucedida com a API do Gemini
- ✅ Respostas geradas para ambas as perguntas
- ⚠️ **Limitação**: O chatbot não mantém contexto entre perguntas. Na segunda pergunta, ele não lembra que estava falando sobre Python na primeira.

---

### **Etapa #2: Personalidade e Estrutura do Chatbot**

#### 🎯 Objetivo

Dar personalidade ao chatbot através de um template de prompt estruturado, transformando-o no "GeoAI Mentor" especializado.

#### 📝 Requisitos Implementados

1. ✅ Importação de `ChatPromptTemplate` e `StrOutputParser`
2. ✅ Criação de template com três componentes:
   - Mensagem de sistema (personalidade)
   - Placeholder para histórico
   - Mensagem do usuário (query)
3. ✅ Criação de cadeia (chain) usando LCEL (LangChain Expression Language)

#### 💻 Código da Etapa #2

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Instancia o modelo Gemini
modelo = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# Cria o template de prompt com personalidade do GeoAI Mentor
template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático."),
    ("placeholder", "{historico}"),
    ("human", "{query}")
])

# Cria a cadeia (chain) usando LCEL
chain = template | modelo | StrOutputParser()

# Lista de perguntas sequenciais
perguntas = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
]

# Loop que envia cada pergunta para o modelo e imprime a resposta
for pergunta in perguntas:
    print(f"\n🔵 Pergunta: {pergunta}")
    # Usa a chain com histórico vazio (será implementado nas próximas etapas)
    resposta = chain.invoke({"query": pergunta, "historico": []})
    print(f"\n🤖 GeoAI Mentor: {resposta}")
    print("-" * 80)
```

#### 📊 Resultado da Etapa #2

- ✅ Chatbot com personalidade definida
- ✅ Respostas mais amigáveis e didáticas
- ✅ Foco em geocientistas e exemplos específicos da área
- ⚠️ **Limitação**: Ainda não mantém contexto entre perguntas (histórico está vazio)

#### 🔍 Conceitos LCEL (LangChain Expression Language)

O operador `|` (pipe) cria uma cadeia de processamento:

```python
chain = template | modelo | StrOutputParser()
```

**Fluxo de execução:**

1. `template` → Formata a entrada com o prompt estruturado
2. `modelo` → Processa com o Gemini
3. `StrOutputParser()` → Extrai apenas o texto da resposta

---

### **Etapa #3: Memória Conversacional (Final)**

#### 🎯 Objetivo

Implementar a capacidade de memória conversacional, permitindo que o chatbot lembre de interações anteriores e mantenha contexto ao longo da conversa.

#### 📝 Requisitos Implementados

1. ✅ Importação de `InMemoryChatMessageHistory` e `RunnableWithMessageHistory`
2. ✅ Criação de dicionário `memoria_sessoes` para armazenar históricos
3. ✅ Implementação da função `obter_historico_por_sessao()` com padrão singleton
4. ✅ Criação de `cadeia_com_memoria` usando `RunnableWithMessageHistory`
5. ✅ Modificação do loop para usar a cadeia com memória e `session_id`

#### 💻 Código da Etapa #3 (Final)

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Instancia o modelo Gemini
modelo = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# Cria o template de prompt com personalidade do GeoAI Mentor
template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático."),
    ("placeholder", "{historico}"),
    ("human", "{query}")
])

# Cria a cadeia (chain) usando LCEL
chain = template | modelo | StrOutputParser()

# Dicionário para armazenar o histórico de cada sessão
memoria_sessoes = {}

# Função para obter ou criar histórico por sessão (padrão singleton)
def obter_historico_por_sessao(session_id: str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]

# Cria a cadeia com memória
cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)

# Lista de perguntas sequenciais
perguntas = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
]

# Configuração da sessão
config = {"configurable": {"session_id": "sessao_geocientista_01"}}

# Loop que envia cada pergunta para o modelo e imprime a resposta
for pergunta in perguntas:
    print(f"\n🔵 Pergunta: {pergunta}")
    # Usa a cadeia com memória
    resposta = cadeia_com_memoria.invoke({"query": pergunta}, config=config)
    print(f"\n🤖 GeoAI Mentor: {resposta}")
    print("-" * 80)

# Exibe o histórico completo da conversa
print("\n" + "=" * 80)
print("📝 HISTÓRICO DA CONVERSA:")
print("=" * 80)
historico = obter_historico_por_sessao("sessao_geocientista_01")
for mensagem in historico.messages:
    tipo = "👤 Usuário" if mensagem.type == "human" else "🤖 GeoAI Mentor"
    print(f"\n{tipo}: {mensagem.content[:100]}...")
print("=" * 80)
```

#### 📊 Resultado da Etapa #3

- ✅ Chatbot mantém contexto completo da conversa
- ✅ Segunda pergunta compreende que está falando sobre Python
- ✅ Sugestões de projetos específicas para Python e geofísica
- ✅ Histórico da conversa armazenado e recuperável
- ✅ Suporte para múltiplas sessões independentes

#### 🔍 Conceitos de Memória

**Padrão Singleton:**

```python
def obter_historico_por_sessao(session_id: str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]
```

Garante que cada `session_id` tenha uma única instância de histórico.

**RunnableWithMessageHistory:**

- Envelopa a cadeia existente
- Injeta automaticamente o histórico no placeholder
- Salva novas mensagens após cada interação

---

## 📈 Comparativo das Etapas

| Aspecto               | Etapa #1 | Etapa #2 | Etapa #3 |
| --------------------- | -------- | -------- | -------- |
| **Conexão API**       | ✅       | ✅       | ✅       |
| **Personalidade**     | ❌       | ✅       | ✅       |
| **Estrutura LCEL**    | ❌       | ✅       | ✅       |
| **Memória**           | ❌       | ❌       | ✅       |
| **Contexto**          | ❌       | ❌       | ✅       |
| **Múltiplas Sessões** | ❌       | ❌       | ✅       |

---

## 🎓 Conceitos Importantes Aprendidos

### 1. **LangChain Expression Language (LCEL)**

Sintaxe declarativa para criar cadeias de processamento usando o operador `|`:

```python
chain = template | modelo | StrOutputParser()
```

### 2. **Templates de Prompt**

Estruturam a conversa em três partes:

- **System**: Define personalidade e instruções
- **Placeholder**: Espaço para histórico dinâmico
- **Human**: Entrada do usuário

### 3. **Gerenciamento de Memória**

- `InMemoryChatMessageHistory`: Armazena mensagens em memória
- `RunnableWithMessageHistory`: Gerencia injeção automática de histórico
- `session_id`: Permite múltiplas conversas independentes

### 4. **Padrão Singleton**

Garante uma única instância de histórico por sessão:

```python
if session_id not in memoria_sessoes:
    memoria_sessoes[session_id] = InMemoryChatMessageHistory()
return memoria_sessoes[session_id]
```

---

## 🔧 Arquivos do Projeto

```
MyGeoAI_Mentor/
├── .env                          # Chave de API do Google Gemini
├── chatbot_mentor.py             # Código principal (Etapa #3 final)
├── requirements.txt              # Dependências do projeto
├── README.md                     # Instruções de uso
├── DOCUMENTACAO_COMPLETA.md      # Este arquivo
└── listar_modelos.py             # Script auxiliar para listar modelos
```

---

## 🎯 Conclusão

O projeto **GeoAI Mentor** evoluiu através de três etapas bem definidas:

### ✨ Conquistas

1. **Etapa #1**: Estabelecemos conexão funcional com o Gemini e validamos a comunicação básica
2. **Etapa #2**: Adicionamos personalidade e estrutura profissional ao chatbot
3. **Etapa #3**: Implementamos memória conversacional completa

### 🚀 Resultado Final

Um chatbot especializado que:

- ✅ Mantém contexto ao longo da conversa
- ✅ Fornece respostas personalizadas para geocientistas
- ✅ É amigável e didático
- ✅ Suporta múltiplas sessões independentes
- ✅ Utiliza o modelo mais recente do Gemini (2.0-flash)

### 💡 Aplicações Práticas

O GeoAI Mentor pode ser expandido para:

- Interface web com Streamlit ou Gradio
- Chatbot em plataformas de mensagem (WhatsApp, Telegram)
- Sistema de mentoria para empresas de geociências
- Plataforma educacional para cursos online
- Assistente de orientação de carreira

### 🎓 Habilidades Desenvolvidas

- ✅ Integração com APIs de IA generativa (Google Gemini)
- ✅ Uso do framework LangChain
- ✅ Gerenciamento de memória conversacional
- ✅ Estruturação de prompts eficazes
- ✅ Padrões de design (Singleton)
- ✅ Desenvolvimento de aplicações com IA

### 🔮 Próximos Passos Sugeridos

1. **Interface Gráfica**: Criar interface web com Streamlit
2. **Persistência**: Salvar histórico em banco de dados
3. **RAG (Retrieval-Augmented Generation)**: Adicionar base de conhecimento específica
4. **Multi-agentes**: Criar agentes especializados em diferentes áreas
5. **Análise de Sentimento**: Adaptar respostas ao estado emocional do usuário
6. **Feedback Loop**: Implementar sistema de avaliação das respostas
7. **Deploy**: Publicar na nuvem (AWS, Google Cloud, Azure)

---

## 📚 Recursos Adicionais

### Documentação Oficial

- [Google Gemini AI](https://ai.google.dev/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Google GenAI](https://python.langchain.com/docs/integrations/llms/google_ai)

### Tutoriais Recomendados

- [LangChain Quickstart](https://python.langchain.com/docs/get_started/quickstart)
- [Building Chatbots with Memory](https://python.langchain.com/docs/expression_language/how_to/message_history)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## 👨‍💻 Autor

Projeto desenvolvido como parte do desafio de criação de chatbot especializado para geocientistas.

**Data de Conclusão**: 02 de Dezembro de 2025

---

## ✅ Pontos de Revisão e Validação

Ao concluir o projeto, é importante verificar se não cometeu algum destes erros comuns:

### 🔑 1. Chave de API

**⚠️ Atenção**: Como estamos usando **Google Gemini** (não OpenAI), a configuração é diferente:

- ✅ **Correto para Gemini**: `GOOGLE_API_KEY="sua_chave_aqui"`
- ❌ **Errado**: `OPENAI_API_KEY="sua_chave_aqui"` (isso é para OpenAI/ChatGPT)

**Verificações:**

- [ ] A variável no arquivo `.env` está como `GOOGLE_API_KEY`?
- [ ] A função `load_dotenv()` foi chamada no início do script?
- [ ] A chave foi obtida em https://aistudio.google.com/app/apikey?

**Código de verificação:**

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key carregada: {api_key[:10]}..." if api_key else "❌ API Key não encontrada!")
```

### 🔗 2. Consistência das Chaves no Template

**Verificações críticas:**

Os nomes das variáveis no `ChatPromptTemplate` devem corresponder exatamente aos parâmetros do `RunnableWithMessageHistory`:

```python
# ✅ CORRETO - As chaves devem ser IDÊNTICAS
template = ChatPromptTemplate.from_messages([
    ("system", "..."),
    ("placeholder", "{historico}"),    # Nome: "historico"
    ("human", "{query}")               # Nome: "query"
])

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",        # Mesmo nome: "query"
    history_messages_key="historico"   # Mesmo nome: "historico"
)
```

**Checklist:**

- [ ] O placeholder no template está como `{historico}`?
- [ ] O `history_messages_key` está como `"historico"`?
- [ ] A mensagem human no template está como `{query}`?
- [ ] O `input_messages_key` está como `"query"`?

### 📞 3. Estrutura Correta do invoke()

**Estrutura obrigatória para cadeia com memória:**

```python
# ✅ CORRETO
resposta = cadeia_com_memoria.invoke(
    {"query": pergunta},                                    # Dicionário com a pergunta
    config={"configurable": {"session_id": "sessao_01"}}   # Config com session_id
)

# ❌ ERRADO - Sem config
resposta = cadeia_com_memoria.invoke({"query": pergunta})

# ❌ ERRADO - Config mal estruturado
resposta = cadeia_com_memoria.invoke({"query": pergunta}, {"session_id": "sessao_01"})
```

**Checklist:**

- [ ] O `invoke()` recebe dois argumentos?
- [ ] O primeiro argumento é um dicionário com a chave `"query"`?
- [ ] O segundo argumento é `config={"configurable": {"session_id": "..."}}`?
- [ ] O `session_id` está definido como string?

### 🧠 4. Validação da Memória

**Teste prático para confirmar que a memória está funcionando:**

Execute as duas perguntas sequenciais e observe:

**Pergunta 1:**

```
"Eu sou geofísico e quero migrar para a área de dados.
Qual linguagem de programação devo aprender primeiro?"
```

**Resposta esperada:** O chatbot recomenda **Python** com justificativas.

**Pergunta 2:**

```
"E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
```

**✅ Memória FUNCIONANDO** se:

- O chatbot menciona projetos específicos de **Python**
- Não pergunta "qual linguagem?"
- Sugere projetos relacionados a geofísica + Python
- Demonstra continuidade da conversa

**❌ Memória NÃO FUNCIONANDO** se:

- O chatbot pergunta qual linguagem você quer usar
- Dá sugestões genéricas sem mencionar Python
- Não há continuidade lógica entre as respostas

### 🔍 5. Debug do Histórico

**Script para visualizar o histórico:**

```python
# Adicione ao final do seu código para debug
historico = obter_historico_por_sessao("sessao_geocientista_01")
print(f"\n📊 Total de mensagens no histórico: {len(historico.messages)}")
for i, msg in enumerate(historico.messages, 1):
    tipo = "👤" if msg.type == "human" else "🤖"
    print(f"{tipo} Mensagem {i}: {msg.content[:80]}...")
```

**Saída esperada para 2 perguntas:**

```
📊 Total de mensagens no histórico: 4
👤 Mensagem 1: Eu sou geofísico e quero migrar...
🤖 Mensagem 2: Olá! Que excelente escolha!...
👤 Mensagem 3: E que tipo de projeto de portfólio...
🤖 Mensagem 4: Excelente pergunta! Projetos de portfólio...
```

### 🎯 6. Checklist Final

Antes de considerar o projeto concluído, verifique:

**Arquivos:**

- [ ] `.env` existe e contém `GOOGLE_API_KEY`
- [ ] `chatbot_mentor.py` está com o código da Etapa #3
- [ ] `requirements.txt` contém todas as dependências
- [ ] `README.md` tem instruções claras

**Código:**

- [ ] Todas as importações estão corretas
- [ ] `load_dotenv()` é chamado antes de usar a API
- [ ] Template tem system, placeholder e human
- [ ] Chain usa LCEL: `template | modelo | StrOutputParser()`
- [ ] Função `obter_historico_por_sessao()` implementada
- [ ] `RunnableWithMessageHistory` configurado corretamente
- [ ] Loop usa `cadeia_com_memoria.invoke()` com config

**Funcionalidade:**

- [ ] Código executa sem erros
- [ ] Primeira pergunta recebe resposta adequada
- [ ] Segunda pergunta mantém contexto da primeira
- [ ] Histórico é armazenado corretamente
- [ ] Múltiplas sessões podem coexistir

### 🐛 Erros Comuns e Soluções

| Erro                                              | Causa                  | Solução                                              |
| ------------------------------------------------- | ---------------------- | ---------------------------------------------------- |
| `404 models/gemini-pro is not found`              | Modelo não disponível  | Use `gemini-2.0-flash`                               |
| `cannot import name 'InMemoryChatMessageHistory'` | Import incorreto       | Import de `langchain_core.chat_history`              |
| `KeyError: 'query'`                               | Nome inconsistente     | Verifique que todos os `"query"` são idênticos       |
| `Session not found`                               | Config mal estruturado | Use `config={"configurable": {"session_id": "..."}}` |
| Contexto não mantido                              | Histórico vazio        | Verifique se está usando `cadeia_com_memoria`        |

---

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

---

**🎉 Parabéns por concluir o projeto GeoAI Mentor! 🎉**

Se seguiu todos os pontos de revisão acima, seu chatbot está funcionando perfeitamente com memória conversacional completa! 🚀
