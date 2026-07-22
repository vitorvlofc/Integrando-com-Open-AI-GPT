import base64
from datetime import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente definidas no arquivo .env para a memória da aplicação
load_dotenv()

# Instancia o cliente da OpenAI. Ele busca automaticamente pela variável OPENAI_API_KEY no ambiente
client = OpenAI()

# Define o prompt em texto que descreve os detalhes da imagem a ser gerada
prompt = "gere uma imagem de uma paisagem a onde a natureza predomina de forma exuberante, com árvores altas, flores coloridas e um rio cristalino refletindo o céu azul."

# Faz a chamada para a API de geração de imagens com os parâmetros de modelo, tamanho e qualidade
response = client.images.generate(
    model="dall-e-3",  # Modelo de geração de imagem da OpenAI (nota: verifique o nome do modelo suportado)
    prompt=prompt,     # Descrição do que deve ser gerado
    size="1024x1024",  # Dimensões da imagem a ser criada
    quality="standard", # Qualidade da imagem (ex: "standard" ou "hd")
    n=1,               # Quantidade de imagens a serem geradas
)

# Extrai a string codificada em Base64 do primeiro objeto retornado na resposta
image_base64 = response.data[0].b64_json

# Decodifica a string Base64 de volta para o formato binário de imagem (bytes)
image_bytes = base64.b64decode(image_base64)

# Cria a pasta 'outputs' caso ela ainda não exista no projeto
os.makedirs("outputs", exist_ok=True)

# Define o caminho do arquivo gerando um nome único baseado na data e hora atual
file_path = f"outputs/img_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

# Escreve os bytes decodificados diretamente no disco no formato binário ("wb")
with open(file_path, "wb") as f:
    f.write(image_bytes)

# Exibe no console a confirmação do local onde o arquivo foi salvo
print(f"Imagem salva em: {file_path}")
