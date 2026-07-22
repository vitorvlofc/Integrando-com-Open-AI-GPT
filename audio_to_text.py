from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Abre o arquivo de áudio no modo de leitura binária ("rb"), necessário para envio de arquivos
with open("output_audio.mp3", "rb") as audio_file:
    # Faz a requisição para a API de transcrição (Speech-to-Text) usando o modelo Whisper
    transcription = client.audio.transcriptions.create(
        model="whisper-1",  # Modelo oficial de reconhecimento e transcrição de áudio
        file=audio_file     # O arquivo de áudio a ser transcrito
    )

# Extrai o texto transcrito do objeto de resposta retornado pela API
text = transcription.text

# Exibe o texto transcrito no terminal
print(text)

# Abre (ou cria) um arquivo de texto no modo de escrita ("w") com codificação UTF-8 para suportar acentuação
with open("transcricao.txt", "w", encoding="utf-8") as f:
    # Salva o texto transcrito no arquivo no disco
    f.write(text)
