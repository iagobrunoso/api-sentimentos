📌 API de Análise de Sentimentos

Esta é uma API simples desenvolvida com FastAPI para análise básica de sentimentos em textos. Ela classifica mensagens como positivo, negativo ou neutro, com base em palavras-chave.

**🚀 Tecnologias utilizadas**

Python 3.11
FastAPI
Uvicorn
Docker
GitHub Actions

**📂 Estrutura do projeto**
.
├── main.py
├── requirements.txt
├── Dockerfile
└── .github/workflows/pipeline.yml

▶️ Como executar o projeto localmente (sem Docker)

**1. Clone o repositório**

git clone https://github.com/iagobrunoso/api-sentimentos.git
cd api-sentimentos

**2. Crie um ambiente virtual (opcional, mas recomendado)**

python3 -m venv venv
source venv/bin/activate  # Mac/Linux

**3. Instale as dependências**

pip install -r requirements.txt

**4. Execute a aplicação**

uvicorn main:app --reload

**5. Acesse no navegador**

- API: http://localhost:8000
- Documentação interativa: http://localhost:8000/docs

**🐳 Como executar com Docker**

**1. Build da imagem**

docker build -t api-sentimentos

**2. Rodar o container**

docker run -p 8000:8000 api-sentimentos

**3. Acessar**

http://localhost:8000
http://localhost:8000/docs

**📡 Endpoints da API**

**🔹 GET /**
Retorna mensagem de status da API

Resposta:
{
  "mensagem": "API de análise de sentimentos funcionando"
}

**🔹 POST /analisar**
Analisa o sentimento de uma frase

Exemplo de requisição:
{
  "mensagem": "Hoje foi um dia bom"
}

Resposta:
{
  "texto": "Hoje foi um dia bom",
  "sentimento": "positivo"
}

**⚙️ Regras de análise**

Contém "bom" → positivo
Contém "ruim" → negativo
Caso contrário → neutro

**🔄 CI/CD com GitHub Actions**

O projeto possui uma pipeline configurada que:
Executa após merge de Pull Request
Faz build da imagem Docker
Realiza login no Docker Hub
Publica a imagem automaticamente

**🔐 Variáveis de ambiente (GitHub Secrets)**

Necárias para a pipeline:

DOCKER_USERNAME
DOCKER_PASSWORD

**🐳 Imagem no Docker Hub**

A imagem da aplicação está disponível em:

iagobruno2702/api-sentimentos:latest

**📌 Observações**

A API utiliza uma lógica simples para fins didáticos
Pode ser expandida com modelos reais de NLP (como NLP com IA)
Ideal para estudos de CI/CD, Docker e deploy

**👨‍💻 Autor**

Iago Bruno
Patricia San Izidro
Fábio Rios

