# 🎬 Guia para Criar Demo Visual do GeoAI Mentor

## 🎯 Objetivo

Criar material visual impactante para o portfólio no GitHub, demonstrando o poder da memória conversacional.

---

## 📸 Opção 1: Criar GIF Animado (Recomendado)

### Ferramentas Necessárias

**Windows:**

- [ScreenToGif](https://www.screentogif.com/) - Gratuito e fácil de usar

**Multiplataforma:**

- [OBS Studio](https://obsproject.com/) + [FFmpeg](https://ffmpeg.org/)
- [LICEcap](https://www.cockos.com/licecap/)

### Passo a Passo com ScreenToGif

1. **Preparação:**

   ```bash
   # Limpe o terminal
   cls  # ou clear no Linux/Mac

   # Teste o chatbot antes
   python chatbot_mentor.py
   ```

2. **Grave a Demonstração:**

   - Abra ScreenToGif
   - Clique em "Recorder"
   - Posicione sobre o terminal PowerShell
   - Pressione F7 para iniciar gravação
   - Execute: `python chatbot_mentor.py`
   - Aguarde as 2 respostas completas
   - Pressione F8 para parar

3. **Edite o GIF:**
   - Delete frames iniciais (carregamento)
   - Adicione texto destacando:
     - "🔵 Primeira Pergunta"
     - "✅ Recomenda Python"
     - "🔵 Segunda Pergunta"
     - "🎯 Lembra de Python!"
   - Salve como `demo.gif` na pasta `assets/`

### Dicas para Melhor Qualidade

```bash
# Configure o terminal para melhor legibilidade
# Aumente a fonte (Ctrl + ou Ctrl Scroll Up)
# Use tema escuro para contraste
# Mantenha janela em tamanho médio (não tela cheia)
```

---

## 🖼️ Opção 2: Criar Screenshots Comparativos

### Script para Capturar Momentos-Chave

```python
# capturar_demo.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

modelo = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático."),
    ("placeholder", "{historico}"),
    ("human", "{query}")
])

chain = template | modelo | StrOutputParser()

print("=" * 80)
print("DEMONSTRAÇÃO: SEM MEMÓRIA (Etapa #1)")
print("=" * 80)

# Primeira interação sem memória
print("\n👤 Pergunta 1: Qual linguagem de programação devo aprender primeiro?")
resposta1 = modelo.invoke("Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?")
print(f"\n🤖 {resposta1.content[:200]}...")

input("\n[Pressione ENTER para continuar...]")

print("\n👤 Pergunta 2: Que projetos posso criar com essa linguagem?")
resposta2 = modelo.invoke("E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?")
print(f"\n🤖 {resposta2.content[:200]}...")

if "qual linguagem" in resposta2.content.lower() or "me diga" in resposta2.content.lower():
    print("\n⚠️  PROBLEMA: O chatbot NÃO LEMBRA da primeira pergunta!")
    print("❌ Ele está pedindo para especificar a linguagem novamente.")

input("\n[Pressione ENTER para demonstração COM MEMÓRIA...]")

# Agora com memória
memoria_sessoes = {}

def obter_historico_por_sessao(session_id: str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)

config = {"configurable": {"session_id": "demo_session"}}

print("\n" + "=" * 80)
print("DEMONSTRAÇÃO: COM MEMÓRIA (Etapa #3)")
print("=" * 80)

print("\n👤 Pergunta 1: Qual linguagem de programação devo aprender primeiro?")
resposta1_mem = cadeia_com_memoria.invoke(
    {"query": "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?"},
    config=config
)
print(f"\n🤖 {resposta1_mem[:200]}...")

input("\n[Pressione ENTER para segunda pergunta...]")

print("\n👤 Pergunta 2: Que projetos posso criar com essa linguagem?")
resposta2_mem = cadeia_com_memoria.invoke(
    {"query": "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"},
    config=config
)
print(f"\n🤖 {resposta2_mem[:200]}...")

if "python" in resposta2_mem.lower():
    print("\n✅ SUCESSO: O chatbot LEMBRA que estávamos falando de Python!")
    print("🎯 Ele forneceu sugestões específicas para Python sem precisar perguntar!")

print("\n" + "=" * 80)
print("📊 HISTÓRICO DA CONVERSA:")
print("=" * 80)
historico = obter_historico_por_sessao("demo_session")
print(f"Total de mensagens armazenadas: {len(historico.messages)}")
for i, msg in enumerate(historico.messages, 1):
    tipo = "👤 Usuário" if msg.type == "human" else "🤖 GeoAI"
    print(f"{i}. {tipo}: {msg.content[:80]}...")
```

### Capturando Screenshots

**No Windows:**

- `Win + Shift + S` → Ferramenta de recorte
- Capture:
  1. Terminal antes (sem memória) - `sem_memoria.png`
  2. Terminal depois (com memória) - `com_memoria.png`
  3. Exibição do histórico - `historico.png`

---

## 📊 Criar Diagrama de Arquitetura

### Usando Draw.io (Recomendado)

1. Acesse [draw.io](https://app.diagrams.net/)
2. Crie novo diagrama
3. Use formas para representar:

```
┌─────────────────────┐
│   Usuário Digita    │
│     Pergunta        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ ChatPromptTemplate  │
│  ┌──────────────┐   │
│  │ System Msg   │   │
│  │ History ◄────┼───┼─── Injeta memória
│  │ Human Msg    │   │
│  └──────────────┘   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Gemini 2.0 AI     │
│   (Processa)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  StrOutputParser    │
│  (Formata Texto)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Resposta       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ InMemoryChat        │
│ MessageHistory      │
│  (Salva Histórico)  │
└─────────────────────┘
```

4. Exporte como PNG → `assets/arquitetura.png`

---

## 📝 Criar Imagem de Comparação

### Template para Comparação

Crie um arquivo Markdown para depois converter em imagem:

```markdown
# Antes vs Depois: Poder da Memória

## ❌ SEM MEMÓRIA (Etapa #1)

**Pergunta 1:**

> Qual linguagem aprender?

**Resposta:**

> Python é recomendado...

**Pergunta 2:**

> Que projetos criar?

**Resposta:**

> 😕 Qual linguagem você quer usar?

### Problema: Não lembra!

---

## ✅ COM MEMÓRIA (Etapa #3)

**Pergunta 1:**

> Qual linguagem aprender?

**Resposta:**

> Python é recomendado...

**Pergunta 2:**

> Que projetos criar?

**Resposta:**

> 🎯 Com Python você pode:
>
> - Análise sísmica
> - Modelagem ML
> - Mapas interativos

### Sucesso: Mantém contexto!
```

### Converter para Imagem

**Opção 1: Carbon.now.sh**

- Acesse [carbon.now.sh](https://carbon.now.sh/)
- Cole o texto
- Ajuste tema e cores
- Export → `comparacao.png`

**Opção 2: Screenshot de Editor**

- Abra no VS Code com preview
- Capture tela lado a lado
- Salve como `comparacao.png`

---

## 🎨 Organização dos Assets

```bash
# Crie a pasta
mkdir assets

# Estrutura final:
assets/
├── demo.gif              # GIF animado da demonstração
├── arquitetura.png       # Diagrama da arquitetura
├── comparacao.png        # Antes vs Depois
├── sem_memoria.png       # Screenshot sem memória
├── com_memoria.png       # Screenshot com memória
└── historico.png         # Screenshot do histórico
```

---

## 📋 Checklist Final

Antes de publicar no GitHub:

- [ ] GIF criado e testado (< 10MB)
- [ ] Diagrama de arquitetura claro
- [ ] Comparação visual impactante
- [ ] Screenshots em alta resolução
- [ ] Todos os arquivos na pasta `assets/`
- [ ] README.md atualizado com links para imagens
- [ ] .gitignore configurado (não commitar .env)

---

## 🚀 Publicar no GitHub

```bash
# Adicione os assets
git add assets/

# Commit
git commit -m "docs: adiciona material visual de demonstração"

# Push
git push origin main
```

---

## 💡 Dicas Finais

1. **GIF deve ser curto:** 30-60 segundos máximo
2. **Texto no GIF:** Use contraste alto
3. **Qualidade vs Tamanho:** Prefira qualidade, mas mantenha < 10MB
4. **GitHub suporta GIF:** Funcionará diretamente no README
5. **Teste visualização:** Veja no GitHub após upload

---

**Boa sorte com seu portfólio! 🎉**
