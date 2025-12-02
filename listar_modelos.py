import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega as variáveis de ambiente
load_dotenv()

# Configura a API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Lista todos os modelos disponíveis
print("Modelos disponíveis:\n")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Nome: {model.name}")
        print(f"Display Name: {model.display_name}")
        print(f"Métodos suportados: {model.supported_generation_methods}")
        print("-" * 80)
