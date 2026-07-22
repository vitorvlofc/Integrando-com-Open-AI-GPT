from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Faz a requisição ativando o modo streaming e definindo mensagens com papéis (system e user)
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Especifica o modelo a ser utilizado
    messages=[
        # Define a persona/comportamento base do assistente
        {"role": "system", "content": "Vocé é um assistente especialista em base de programação em python explicativa de forma clara é simples."},
        # Define a pergunta/solicitação do usuário
        {"role": "user", "content": "me explica um pouco sobre a função print() do python. e me mostre um exemplo basico de logica de programação"},
    ],
    stream=True,  # Habilita a transmissão progressiva da resposta em tempo real
)

# Percorre cada fragmento (chunk) recebido do fluxo de resposta
for chunk in stream:
    # Garante que o fragmento possui texto antes de tentar imprimir (evita None)
    if chunk.choices[0].delta.content is not None:
        # Exibe o texto recebido mantendo o fluxo contínuo na mesma linha do terminal
        print(chunk.choices[0].delta.content, end='')
