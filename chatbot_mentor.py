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
