FROM python:3.11-slim

# Instala o Poetry
RUN pip install poetry

# Configura o ambiente de trabalho
WORKDIR /code

# Copia os arquivos de definição do projeto
COPY pyproject.toml poetry.lock /code/

COPY . /code/
# Instala as dependências do projeto
RUN poetry install --no-interaction --no-ansi

# Copia o restante do código do projeto

# Comando padrão para executar o projeto
CMD poetry run python manage.py runserver 0.0.0.0:8000
