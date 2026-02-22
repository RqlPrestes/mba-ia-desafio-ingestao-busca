# Desafio MBA Engenharia de Software com IA - Full Cycle

Descreva abaixo como executar a sua solução.

1- Criar e ativar um ambiente virtual (venv):

python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

2 - Instalar as dependências:

pip install -r requirements.txt


Ordem de execução


Subir o banco de dados:

1 - docker compose up -d

Executar ingestão do PDF:

2 - python src/ingest.py

Rodar o chat:

3 - python src/chat.py