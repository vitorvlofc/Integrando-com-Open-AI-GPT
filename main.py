from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Faz a requisição em streaming configurando diretrizes, controle de tamanho e criatividade
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Especifica o modelo a ser utilizado
    messages=[
        # Define a instrução de sistema que limita o papel da IA a tradutor de texto
        {"role": "system", "content": "Vocé será um tradutor de texto para português."},
        # Envia o texto fornecido pelo usuário a ser processado
        {"role": "user", "content": "meu nome é vitor"},
    ],
    stream=True,         # Habilita o envio progressivo da resposta em tempo real
    max_tokens=200,      # Limita o tamanho máximo da resposta gerada a 200 tokens
    temperature=0.2,     # Define baixa variabilidade/criatividade (respostas mais diretas e precisas)
)

# Percorre cada fragmento (chunk) recebido do fluxo de resposta
for chunk in stream:
    # Verifica se o fragmento atual possui conteúdo de texto válido
    if chunk.choices[0].delta.content is not None:
        # Exibe o texto recebido de forma contínua no terminal
        print(chunk.choices[0].delta.content, end='')
