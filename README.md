# TS: sistema gerenciamento de seller e marketplace.

## Descrição

Desafio: sistema gerenciamento de seller e marketplace com teste unitário e verificação de cobertura de testes.

Construído sobre uma plataforma Python 3, Poetry, Pytest, Python-decouple, Docker, Docker-Compose, Postgresql

## Instruções instalação e execução com docker-compose:

- Configure as opções de: migrations, user_admin, pytest (com ou sem relatório) e runserver, em:

> scripts/run.sh

- No terminal execute:

```sh
docker-compose up
```

## Instruções de instalação local:

- Instale o Python:

```sh
pyenv local 3.9.5
```

- Configure o ambiente virtual:

```sh
poetry install
```

- Acesse o ambiente virtual:

```sh
poetry shell
```

## Autor(es):
- Danilo e Jeff.