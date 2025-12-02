# 🌍 GeoAI Mentor - Assistente IA para Transição de Carreira em Geociências

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![Google Gemini](https://img.shields.io/badge/Gemini-2.0--flash-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Um chatbot inteligente especializado em orientar geocientistas na migração para Ciência de Dados e IA**

[Demonstração](#-demonstração) • [Instalação](#-instalação-rápida) • [Como Usar](#-como-usar) • [Arquitetura](#-arquitetura-técnica) • [Documentação](DOCUMENTACAO_COMPLETA.md)

</div>

---

## 🎯 O Problema

Muitos **geofísicos e geólogos** possuem forte base em matemática e física, mas enfrentam dificuldades ao migrar para **Ciência de Dados e IA**. As principais dúvidas incluem:

- 🤔 Quais linguagens de programação aprender?
- 📚 Como transferir conhecimentos da área de geociências?
- 💼 Que projetos criar para um portfólio atrativo?
- 🎓 Quais cursos e recursos priorizar?

## 💡 A Solução: GeoAI Mentor

Um **chatbot assistente com memória conversacional** que atua como mentor personalizado, lembrando do contexto da conversa para fornecer orientações coesas e relevantes.

### ✨ Diferenciais

- 🧠 **Memória Conversacional**: Mantém contexto entre múltiplas perguntas
- 🎓 **Especializado**: Foco em geocientistas e suas necessidades específicas
- 🤝 **Personalizado**: Respostas adaptadas ao perfil do usuário
- 🔄 **Múltiplas Sessões**: Suporta conversas independentes simultâneas

---

## 🚀 Instalação Rápida

### Pré-requisitos

- Python 3.7 ou superior
- Chave de API do Google Gemini ([Obter gratuitamente](https://aistudio.google.com/app/apikey))

### Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/GeoAI_Mentor.git
cd GeoAI_Mentor

# 2. Crie e ative um ambiente virtual
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure a chave de API
# Edite o arquivo .env e adicione:
# GOOGLE_API_KEY="sua_chave_aqui"
```

---

## 💻 Como Usar

Execute o chatbot:

```bash
python chatbot_mentor.py
```

### Exemplo de Interação

```
🔵 Pergunta: Eu sou geofísico e quero migrar para a área de dados.
              Qual linguagem de programação devo aprender primeiro?

🤖 GeoAI Mentor: Olá! Que excelente escolha! Para começar sua jornada,
                 recomendo Python. É ideal para geocientistas porque...
                 [resposta detalhada sobre Python, NumPy, Pandas, etc.]

─────────────────────────────────────────────────────────────────────

🔵 Pergunta: E que tipo de projeto de portfólio eu poderia criar
              usando essa linguagem?

🤖 GeoAI Mentor: Excelente pergunta! Com Python, você pode criar:
                 1. Análise de dados sísmicos com NumPy e Matplotlib
                 2. Modelagem de reservatórios com machine learning
                 3. Mapas interativos com GeoPandas...
                 [sugestões específicas para Python + Geofísica]
```

---

## 📊 Demonstração: Poder da Memória

### ❌ ANTES (Sem Memória - Etapa #1)

O chatbot **não conecta** as perguntas:

```
👤 Pergunta 1: Qual linguagem de programação devo aprender?
🤖 Resposta: Python é recomendado...

👤 Pergunta 2: Que projetos posso criar com essa linguagem?
🤖 Resposta: Para te dar ideias, preciso saber QUAL LINGUAGEM você está usando...
             ❌ NÃO LEMBRA que acabou de recomendar Python!
```

### ✅ DEPOIS (Com Memória - Etapa #3)

O chatbot **mantém contexto** completo:

```
👤 Pergunta 1: Qual linguagem de programação devo aprender?
🤖 Resposta: Python é recomendado... [detalhes sobre Python]

👤 Pergunta 2: Que projetos posso criar com essa linguagem?
🤖 Resposta: Com PYTHON, você pode criar:
             ✅ LEMBRA do contexto e sugere projetos específicos em Python!
             - Análise de dados sísmicos
             - Modelagem de reservatórios
             - Mapas geoespaciais interativos
```

### 📈 Impacto da Memória

| Aspecto                 | Sem Memória       | Com Memória              |
| ----------------------- | ----------------- | ------------------------ |
| **Continuidade**        | ❌ Perde contexto | ✅ Mantém histórico      |
| **Experiência**         | ❌ Frustrante     | ✅ Natural e fluida      |
| **Relevância**          | ❌ Genérica       | ✅ Personalizada         |
| **Múltiplas conversas** | ❌ Não suporta    | ✅ Sessões independentes |

---

## 🏗️ Arquitetura Técnica

### Visão Geral do Fluxo

```
┌─────────────────┐
│ Entrada Usuário │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│ ChatPromptTemplate  │ ◄─── Injeta histórico da sessão
│ (System + History + │
│      Human)         │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Google Gemini AI   │
│    (2.0-flash)      │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  StrOutputParser    │
│  (Formata saída)    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Resposta Formatada  │ ───► Salva no histórico
└─────────────────────┘
         │
         ▼
┌──────────────────────────┐
│ InMemoryChatMessage      │
│ History (Memória)        │
└──────────────────────────┘
```

### Componentes Principais

#### 1️⃣ **ChatPromptTemplate** - Estrutura da Conversa

Define a **personalidade** e o **formato** das interações:

```python
template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', especializado em..."),
    ("placeholder", "{historico}"),  # Memória dinâmica
    ("human", "{query}")              # Pergunta do usuário
])
```

**Por que é crucial?**

- 🎭 Define a personalidade especializada do chatbot
- 📝 Estrutura consistente para todas as interações
- 🔄 Espaço dedicado para injeção do histórico

#### 2️⃣ **LCEL (LangChain Expression Language)** - Cadeia de Processamento

Sintaxe declarativa que conecta os componentes:

```python
chain = template | modelo | StrOutputParser()
```

**Fluxo de execução:**

1. **Template** → Formata entrada com contexto
2. **Modelo** → Processa com Gemini AI
3. **Parser** → Extrai texto limpo da resposta

#### 3️⃣ **RunnableWithMessageHistory** - Gerenciamento de Memória

O **componente essencial** para memória conversacional:

```python
cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)
```

**Funcionalidades:**

- 💾 Injeta automaticamente histórico no template
- 🔄 Salva novas mensagens após cada interação
- 🎯 Gerencia múltiplas sessões independentes
- 🧠 Transforma IA stateless em stateful

#### 4️⃣ **InMemoryChatMessageHistory** - Armazenamento de Histórico

Implementação com **padrão Singleton**:

```python
memoria_sessoes = {}

def obter_historico_por_sessao(session_id: str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]
```

**Vantagens:**

- ⚡ Rápido (memória RAM)
- 🎯 Uma instância por sessão
- 🔐 Conversas isoladas

### Evolução do Projeto

| Etapa  | Descrição                 | Status          |
| ------ | ------------------------- | --------------- |
| **#1** | Conexão básica com Gemini | ✅ Sem memória  |
| **#2** | Template + Personalidade  | ✅ Estruturado  |
| **#3** | Memória Conversacional    | ✅ **Completo** |

---

## 📁 Estrutura do Projeto

```
GeoAI_Mentor/
│
├── 📄 chatbot_mentor.py          # Código principal (Etapa #3)
├── 📄 listar_modelos.py          # Utilitário para listar modelos Gemini
├── 📄 .env                       # Chave de API (não commitado)
├── 📄 requirements.txt           # Dependências do projeto
│
├── 📖 README.md                  # Este arquivo
├── 📖 DOCUMENTACAO_COMPLETA.md   # Documentação detalhada técnica
│
├── 🖼️ assets/
│   ├── demo.gif                 # Demonstração visual
│   ├── arquitetura.png          # Diagrama da arquitetura
│   └── comparacao.png           # Antes vs Depois
│
└── 🗂️ venv/                     # Ambiente virtual (não commitado)
```

---

## 🎓 Aprendizados e Desafios

### 💡 Principais Insights

1. **ChatPromptTemplate - O Fundamento da Personalidade**

   - Definir o papel do sistema é crucial para respostas consistentes
   - O placeholder `{historico}` permite injeção dinâmica de contexto
   - A estrutura system → history → human cria conversas naturais

2. **O Desafio da Memória Conversacional**

   - LLMs são naturalmente **stateless** (sem estado)
   - Cada chamada é independente, sem "lembrar" do passado
   - Solução: **RunnableWithMessageHistory** adiciona camada de estado

3. **InMemoryChatMessageHistory - Simplicidade e Eficiência**

   - Armazenamento em memória RAM = respostas rápidas
   - Padrão Singleton garante única instância por sessão
   - Trade-off: histórico se perde ao reiniciar (ideal para demos)

4. **IA Sem Estado vs Com Estado**

   | Aspecto      | Sem Estado         | Com Estado            |
   | ------------ | ------------------ | --------------------- |
   | Contexto     | ❌ Não preserva    | ✅ Preserva histórico |
   | Uso          | Perguntas isoladas | Conversas longas      |
   | Complexidade | Simples            | Requer gerenciamento  |
   | Experiência  | Limitada           | Natural e fluida      |

5. **LCEL - Elegância e Poder**
   - Sintaxe com `|` torna código legível
   - Fácil adicionar componentes à cadeia
   - Facilita debugging e manutenção

### 🚀 Desafios Superados

- ✅ Adaptar código de OpenAI para **Google Gemini**
- ✅ Encontrar modelo correto (`gemini-2.0-flash` vs `gemini-pro`)
- ✅ Sincronizar chaves entre template e RunnableWithMessageHistory
- ✅ Implementar estrutura correta do `invoke()` com config
- ✅ Validar que memória realmente está funcionando

---

## 🔮 Próximos Passos

- [ ] Interface web com **Streamlit**
- [ ] Persistência em banco de dados (**PostgreSQL**)
- [ ] **RAG** com base de conhecimento de geociências
- [ ] Deploy na **Google Cloud Run**
- [ ] Testes automatizados
- [ ] Métricas de qualidade das respostas

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13** - Linguagem principal
- **LangChain** - Framework para aplicações LLM
- **Google Gemini 2.0 Flash** - Modelo de linguagem
- **python-dotenv** - Gerenciamento de variáveis de ambiente

---

## 📚 Recursos e Referências

- [Documentação LangChain](https://python.langchain.com/)
- [Google Gemini AI](https://ai.google.dev/)
- [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
- [Building Chatbots with Memory](https://python.langchain.com/docs/expression_language/how_to/message_history)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

## 👤 Autor

**Valter Maurina**

- 💼 LinkedIn: [Seu LinkedIn]
- 🐙 GitHub: [@seu-usuario](https://github.com/seu-usuario)
- 📧 Email: seu.email@example.com

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

---

<div align="center">

**⭐ Se este projeto te ajudou, deixe uma estrela! ⭐**

**🎉 Desenvolvido com dedicação para a comunidade de geocientistas! 🎉**

</div>
