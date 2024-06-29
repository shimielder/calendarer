FROM python3.12

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.8.3 \
  POETRY_VIRTUALENVS_CREATE=false

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry install --no-interaction --no-ansi

ADD . /code

EXPOSE 8000

CMD uvicorn app.main:app --reload --port