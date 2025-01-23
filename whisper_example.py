# imports para o uso do whisper + ollama
from langchain_ollama import OllamaLLM
import whisper


# Carregando o modelo de transcrição de áudio large para maior efetividade com portugues
model = whisper.load_model("large")

# Transcrevendo o áudio e armazenando o texto
result = model.transcribe("react.mp3") 

# salva o texto na variavel do resultado da transcrição
text = result['text']

#carrega o modelo do ollama 
ollama_llm = OllamaLLM(model="llama3.2:1b")

# Prompt para resumir o texto em pontos especificos
prompt = f"Resuma os principais pontos do texto a baixo:\n\n{text}\n\n Retorne os pontos-chave."
response = ollama_llm(prompt)
print(response)
# Prompt para resumir o texto em pontos especificos
prompt = f"Segundo o texto a baixo diga alguns frameworks que usam react :\n\n{text}"
response = ollama_llm(prompt)

print(response)
