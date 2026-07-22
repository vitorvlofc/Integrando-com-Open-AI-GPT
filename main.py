from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Faz a requisição para a API de Chat Completion enviando o modelo e a lista de mensagens
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Especifica o modelo a ser utilizado na resposta
    messages=[
        {"role": "user", "content": "Oque é mais perguntado no chat gpt todo dia."},  # Mensagem enviada pelo usuário
    ],
)

# Imprime o objeto de resposta completo (inclui a mensagem da IA, IDs, modelo, contagem de tokens, etc.)
print(response)

# Imprime apenas o texto puro contido na resposta gerada pelo modelo
print(response.choices[0].message.content)
