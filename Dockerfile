FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y \
       libcairo2 \
       libpango-1.0-0 \
       libpangocairo-1.0-0 \
       libgirepository1.0-dev

RUN pip install poetry

WORKDIR /code

COPY pyproject.toml /code/

COPY . /code/

RUN poetry install --no-interaction --no-ansi