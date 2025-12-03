# 🌍 GeoAI Mentor
## Assistente IA para Transição de Carreira em Geociências

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg?style=flat-square)
![Google Gemini](https://img.shields.io/badge/Gemini-2.0--flash-orange.svg?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

**Um chatbot inteligente e especializado que orienta geocientistas na transição para Ciência de Dados e IA**

</div>

---

## 📋 Índice

- [O Problema](#-o-problema)
- [A Solução](#-a-solução)
- [Recursos](#-recursos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Tecnologias](#-tecnologias)
- [Arquitetura](#-arquitetura)
- [Exemplos](#-exemplos)

---

## 🎯 O Problema

Geocientistas e geofísicos possuem **sólida base em matemática e física**, mas enfrentam desafios ao migrar para **Ciência de Dados e IA**:

- ❓ Qual linguagem de programação aprender?
- ❓ Como aplicar conhecimentos geofísicos em Data Science?
- ❓ Que projetos criar para um portfólio competitivo?
- ❓ Quais recursos e cursos priorizar?

## 💡 A Solução

**GeoAI Mentor** é um chatbot assistente com memória conversacional que funciona como um **mentor personalizado**, mantendo contexto entre perguntas e fornecendo orientações coesas e relevantes.

---

## ✨ Recursos Principais

| Recurso | Descrição |
|---------|-----------|
| 🧠 **Memória Conversacional** | Mantém contexto completo entre múltiplas perguntas |
| 🎓 **Especialização** | Focado especificamente em transição de geocientistas |
| 🤝 **Personalização** | Respostas adaptadas ao perfil e experiência do usuário |
| 🔄 **Múltiplas Sessões** | Suporta conversas independentes simultâneas |
| 📍 **Contextualização** | Exemplos e recomendações baseadas em geofísica/geologia |
| ⚡ **Respostas Detalhadas** | Explicações completas com bibliotecas, ferramentas e exemplos |

---

## 🚀 Instalação

### Pré-requisitos

- **Python 3.8+**
- **Chave de API Google Gemini** ([Obter gratuitamente](https://aistudio.google.com/app/apikey))

### Passos de Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/GeoAI_Mentor.git
cd GeoAI_Mentor

# 2. Crie um ambiente virtual
python -m venv venv

# 3. Ative o ambiente
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Configure a chave de API
# Crie um arquivo .env na raiz do projeto:
echo GOOGLE_API_KEY="sua_chave_aqui" > .env
```

---

## 💻 Como Usar

```bash
python chatbot_mentor.py
```

O chatbot processará automaticamente as perguntas predefinidas e exibirá:
- ✅ Respostas detalhadas com contexto conversacional
- ✅ Histórico completo da conversa ao final
- ✅ Recomendações específicas para geocientistas

---

## 🛠️ Tecnologias

| Tecnologia | Propósito |
|-----------|----------|
| **Python 3.8+** | Linguagem principal |
| **LangChain** | Orquestração de IA e gerenciamento de prompts |
| **Google Gemini 2.0-Flash** | Modelo de linguagem |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |

### Dependências Principais

```
langchain
langchain-google-genai
python-dotenv
```

---

## 🏗️ Arquitetura

```
┌─────────────────────┐
│  Perguntas Input    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────┐
│  Template de Prompt     │
│  (Sistema + Histórico)  │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  LLM Chain (LCEL)       │
│  Gemini 2.0-Flash       │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Memória Conversacional │
│  (InMemoryChatHistory)  │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────┐
│  Resposta Completa  │
└─────────────────────┘
```

---

## 📝 Exemplos

### Exemplo 1: Recomendação de Linguagem

```
🔵 Pergunta: Eu sou geofísico e quero migrar para a área de dados. 
             Qual linguagem de programação devo aprender primeiro?

🤖 GeoAI Mentor: 
Python é a recomendação ideal! Por ser versátil, ter bibliotecas 
especializadas (NumPy, Pandas, GeoPandas), e integração com 
ferramentas geofísicas...
```

### Exemplo 2: Sugestões de Portfólio

```
🔵 Pergunta: E que tipo de projeto de portfólio eu poderia criar?

🤖 GeoAI Mentor:
1. Previsão de Porosidade a partir de Dados Sísmicos
2. Análise de Dados de Poços
3. Classificação de Facies Sedimentares
4. Mapeamento de Anomalias Magnéticas
5. Modelagem de Propagação de Ondas Sísmicas
```

---

## 📁 Estrutura do Projeto

```
GeoAI_Mentor/
├── chatbot_mentor.py      # Script principal
├── requirements.txt       # Dependências Python
├── .env                   # Variáveis de ambiente (não versionado)
├── .gitignore            # Arquivos a ignorar no git
└── README.md             # Este arquivo
```

---

## ⚙️ Configuração

### Arquivo `.env`

```env
GOOGLE_API_KEY="sua_chave_de_api_aqui"
```

**Importante:** Nunca versione o arquivo `.env` em repositórios públicos!

---

## 🔧 Customização

### Modificar Perguntas

Edite a lista `perguntas` em `chatbot_mentor.py`:

```python
perguntas = [
    "Sua primeira pergunta aqui",
    "Sua segunda pergunta aqui",
    "Adicione mais quantas quiser"
]
```

### Ajustar Temperatura da IA

Na instância do modelo, altere o parâmetro `temperature`:

```python
modelo = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7  # 0.0 = determinístico, 1.0 = criativo
)
```

---

## 📊 Saída Esperada

O programa exibe:
1. ✅ Cada pergunta com emoji 🔵
2. ✅ Resposta detalhada com emoji 🤖
3. ✅ Separadores entre perguntas
4. ✅ **Histórico completo** ao final (com 📝)

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma issue ou pull request.

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT - veja detalhes para usar livremente.

---

## 👨‍💻 Autor

Desenvolvido como projeto de demonstração de **IA aplicada à transição de carreira em geociências**.

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se a chave de API está correta no `.env`
2. Confirme que todas as dependências foram instaladas: `pip list`
3. Teste a conexão com: `python -c "import langchain; print('OK')"`

---

**Última atualização:** Dezembro 2025

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
