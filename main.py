from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Faz a requisição ativando o modo streaming (resposta gerada em pedaços em tempo real)
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Especifica o modelo a ser utilizado
    messages=[
        {"role": "user", "content": "Oque é mais perguntado no chat gpt todo dia."},  # Mensagem enviada pelo usuário
    ],
    stream=True,  # Habilita o envio progressivo (stream) da resposta
)

# Percorre cada pedaço (chunk) da resposta à medida que ele chega da API
for chunk in stream:
    # Verifica se o pedaço atual contém texto válido (ignora pedaços vazios ou de controle)
    if chunk.choices[0].delta.content is not None:
        # Imprime o texto do pedaço sem quebra de linha (end='') para formar o texto contínuo no terminal
        print(chunk.choices[0].delta.content, end='')
