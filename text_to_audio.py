from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Faz a requisição para a API de síntese de voz (Text-to-Speech)
response = client.audio.speech.create(
    model="tts-1",  # Modelo de síntese de áudio da OpenAI (ex: "tts-1" ou "tts-1-hd")
    voice="alloy",  # Escolhe o timbre/personalidade da voz (ex: alloy, echo, fable, onyx, nova, shimmer)
    input="A linguagem de programação Python é muito poderosa e versátil ainda mais quando está equipada com ferramentas de inteligência artificial.",  # Texto a ser convertido em fala
)

# Salva o fluxo de áudio gerado diretamente em um arquivo MP3 no disco
response.write_to_file("output_audio.mp3")
