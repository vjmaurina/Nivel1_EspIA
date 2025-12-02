# 📝 Relato de Desenvolvimento - GeoAI Mentor

## 🎯 Visão Geral do Projeto

O **GeoAI Mentor** foi desenvolvido como um chatbot especializado em orientar geocientistas na transição de carreira para Ciência de Dados e IA. O projeto evoluiu em 3 etapas distintas, cada uma adicionando camadas de complexidade e funcionalidade.

---

## 🔄 Jornada de Desenvolvimento

### Etapa #1: Primeiros Passos com LLMs

**Objetivo:** Estabelecer conexão básica com a API do Google Gemini

**Desafios Enfrentados:**

- Adaptação do código de OpenAI para Gemini
- Descoberta do modelo correto disponível (`gemini-2.0-flash`)
- Compreensão da estrutura básica de chamadas à API

**Aprendizado Principal:**

> "Percebi que trabalhar com LLMs modernas requer entender não apenas a API, mas também quais modelos estão disponíveis e suas capacidades específicas."

**Código Chave:**

```python
modelo = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)
resposta = modelo.invoke(pergunta)
```

**Limitação Identificada:**
Sem memória, cada pergunta era tratada de forma isolada. O chatbot não conseguia manter continuidade em conversas.

---

### Etapa #2: Construindo Personalidade

**Objetivo:** Transformar um bot genérico em um mentor especializado

**Momento "Aha!":**

> "O **ChatPromptTemplate** foi revelador! Percebi que a personalidade de uma IA não está apenas nas respostas, mas em como você estrutura o prompt do sistema."

**Implementação Crucial:**

```python
template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', um assistente especializado..."),
    ("placeholder", "{historico}"),
    ("human", "{query}")
])
```

**O que Aprendi:**

1. **System Message** = DNA da IA

   - Define comportamento, tom e expertise
   - Crucial para respostas consistentes

2. **LCEL (LangChain Expression Language)**

   - Sintaxe `|` torna código elegante e legível
   - Facilita manutenção e debugging
   - Permite composição de componentes

3. **Placeholder para Histórico**
   - Reserva espaço para memória futura
   - Preparação arquitetural importante

**Desafio:**
Ainda sem memória real - o placeholder estava vazio. Respostas eram melhores (personalidade), mas sem contexto entre perguntas.

---

### Etapa #3: O Santo Graal - Memória Conversacional

**Objetivo:** Fazer o chatbot "lembrar" do contexto

**O Grande Desafio:**

> "LLMs são naturalmente **stateless** - cada chamada é independente. Como fazer uma IA lembrar de conversas passadas?"

**A Solução: RunnableWithMessageHistory**

Esta foi a descoberta mais impactante do projeto:

```python
cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)
```

**Como Funciona:**

1. **Antes de cada chamada:**

   - Recupera histórico da sessão
   - Injeta no placeholder `{historico}`
   - LLM vê todo o contexto

2. **Após cada resposta:**
   - Salva pergunta e resposta
   - Histórico cresce organicamente
   - Próxima chamada terá mais contexto

**Implementação do Padrão Singleton:**

```python
memoria_sessoes = {}

def obter_historico_por_sessao(session_id: str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]
```

**Por que Singleton?**

- Garante **uma única instância** de histórico por sessão
- Evita duplicação de memória
- Permite múltiplas sessões independentes

---

## 💡 Insights Profundos

### 1. IA Stateless vs Stateful

**Antes de entender isso, eu pensava:**

> "Se eu pergunto algo para uma IA, ela automaticamente lembra"

**Realidade:**

```python
# Sem memória (stateless)
resposta1 = modelo.invoke("Recomende Python")
resposta2 = modelo.invoke("Que projetos criar?")  # ❌ Não sabe que foi Python!

# Com memória (stateful)
resposta1 = cadeia_com_memoria.invoke({"query": "Recomende Python"}, config)
resposta2 = cadeia_com_memoria.invoke({"query": "Que projetos?"}, config)
# ✅ Lembra que foi Python e sugere projetos Python!
```

### 2. A Importância da Estrutura do Prompt

**Descoberta:**

> "80% da qualidade da resposta vem de como você estrutura o prompt, não do modelo em si"

**Estrutura Vencedora:**

```
[SYSTEM] → Define quem a IA é
[HISTORY] → Contexto de mensagens anteriores
[HUMAN] → Pergunta atual do usuário
```

Esta ordem cria uma narrativa natural que o modelo compreende perfeitamente.

### 3. InMemoryChatMessageHistory - Trade-offs

**Vantagens:**

- ⚡ Ultra rápido (RAM)
- 🎯 Simples de implementar
- 🧪 Perfeito para desenvolvimento

**Limitações:**

- 📉 Perde dados ao reiniciar
- 💾 Limitado pela RAM
- 🚫 Não compartilha entre processos

**Quando usar cada tipo:**

- **InMemory:** Demos, protótipos, testes
- **Banco de Dados:** Produção, múltiplos usuários
- **Redis:** Alta performance, sessões distribuídas

---

## 🐛 Erros que Cometi (e Como Resolvi)

### Erro #1: Modelo Não Encontrado

```
404 models/gemini-pro is not found
```

**Causa:** Modelo desatualizado ou nome incorreto

**Solução:**

- Criei script `listar_modelos.py`
- Descobri que `gemini-2.0-flash` era o correto
- Lição: Sempre verificar modelos disponíveis

### Erro #2: Import Incorreto

```python
from langchain.memory import InMemoryChatMessageHistory  # ❌ ERRADO
```

**Solução:**

```python
from langchain_core.chat_history import InMemoryChatMessageHistory  # ✅ CORRETO
```

**Lição:** Documentação do LangChain muda rápido, sempre conferir imports

### Erro #3: Chaves Inconsistentes

```python
# Template tinha {historico}
# Mas configurei history_messages_key="history"  # ❌ INCONSISTENTE
```

**Impacto:** Memória não funcionava - placeholder ficava vazio!

**Solução:**

```python
("placeholder", "{historico}")  # Template
history_messages_key="historico"  # Config - DEVE SER IGUAL!
```

### Erro #4: Estrutura do invoke() Errada

```python
# ❌ ERRADO
cadeia_com_memoria.invoke({"query": pergunta}, {"session_id": "123"})

# ✅ CORRETO
cadeia_com_memoria.invoke(
    {"query": pergunta},
    config={"configurable": {"session_id": "123"}}
)
```

**Lição:** A estrutura aninhada do config não é opcional!

---

## 🎓 O Que Aprendi Sobre IA Conversacional

### 1. Memória é Fundamental para UX

**Exemplo Real do Projeto:**

**Sem Memória (Frustrante):**

```
👤: Qual linguagem aprender?
🤖: Python

👤: Que projetos criar com ela?
🤖: Qual linguagem você quer usar? 😕
```

**Com Memória (Natural):**

```
👤: Qual linguagem aprender?
🤖: Python

👤: Que projetos criar com ela?
🤖: Com Python, você pode criar análise de dados sísmicos... 🎯
```

### 2. Arquitetura em Camadas é Poder

```
Template (Estrutura)
    ↓
Modelo (Inteligência)
    ↓
Parser (Formatação)
    ↓
History (Memória)
```

Cada camada tem responsabilidade clara - facilita manutenção e testes.

### 3. LangChain é uma Abstração Poderosa

**Sem LangChain:**

```python
# Você gerencia:
# - Formatação de prompts
# - Injeção de histórico
# - Parse de respostas
# - Tratamento de erros
# ...muito código boilerplate!
```

**Com LangChain:**

```python
chain = template | modelo | parser
cadeia_com_memoria = RunnableWithMessageHistory(...)
# Abstrações fazem o trabalho pesado!
```

---

## 📊 Impacto Medido

### Testes de Validação da Memória

**Teste 1: Continuidade Contextual**

- ✅ 2ª pergunta referencia corretamente a 1ª
- ✅ Sugestões específicas (Python + Geofísica)
- ✅ Tom consistente de mentor

**Teste 2: Múltiplas Sessões**

```python
# Sessão 1
config_geo = {"configurable": {"session_id": "geo_01"}}

# Sessão 2
config_bio = {"configurable": {"session_id": "bio_01"}}

# ✅ Históricos completamente isolados!
```

**Teste 3: Persistência na Sessão**

- ✅ 4 mensagens armazenadas (2 perguntas + 2 respostas)
- ✅ Ordem cronológica preservada
- ✅ Conteúdo íntegro

---

## 🚀 Próximos Desafios Identificados

### 1. Persistência Real

**Problema:** InMemory perde tudo ao reiniciar

**Solução Planejada:**

```python
# Trocar InMemoryChatMessageHistory por:
from langchain_community.chat_message_histories import PostgresChatMessageHistory

def obter_historico_por_sessao(session_id: str):
    return PostgresChatMessageHistory(
        connection_string="postgresql://...",
        session_id=session_id
    )
```

### 2. Interface Amigável

**Problema:** Terminal é limitado

**Solução Planejada:** Streamlit

```python
import streamlit as st

st.title("🌍 GeoAI Mentor")
user_input = st.chat_input("Sua pergunta...")
# Interface web bonita e interativa!
```

### 3. RAG (Retrieval-Augmented Generation)

**Problema:** Conhecimento limitado ao modelo

**Solução Planejada:**

- Base de conhecimento de artigos de geociências
- PDFs de cursos e tutoriais
- Busca semântica para contexto relevante

---

## 🏆 Conquistas Pessoais

1. ✅ Compreendi profundamente **LLMs stateless vs stateful**
2. ✅ Dominei **LangChain** e LCEL
3. ✅ Implementei **padrão Singleton** na prática
4. ✅ Aprendi **engenharia de prompts** estruturada
5. ✅ Criei projeto **completo e documentado**
6. ✅ Validei **funcionalidade com testes reais**

---

## 💭 Reflexão Final

> "Este projeto transformou minha compreensão sobre IA conversacional. Antes, eu via chatbots como 'mágica'. Agora entendo que são sistemas cuidadosamente arquitetados, onde cada componente - prompt, modelo, parser, memória - tem papel crucial."

**O maior aprendizado:**

> "Memória não é apenas um recurso técnico - é o que transforma uma ferramenta em um companheiro. Um chatbot que lembra do contexto cria conexão, confiança e utilidade real."

**Próximo passo:**
Levar este conhecimento para criar aplicações de IA que realmente façam diferença na vida das pessoas - começando pelos geocientistas que querem migrar de carreira!

---

## 📸 Material Visual Disponível

- `demo.gif` - Demonstração em vídeo do chatbot em ação
- `assets/arquitetura.png` - Diagrama completo da arquitetura
- `assets/comparacao.png` - Antes (sem memória) vs Depois (com memória)
- Capturas de tela dos testes de validação

---

**Desenvolvido com 💙 e muito aprendizado!**

_Valter Maurina - Dezembro 2025_
