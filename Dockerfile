# ---- Base image ----
FROM python:3.14-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3

# ---- Install Poetry ----
RUN pip install "poetry==$POETRY_VERSION"

# ---- Workdir ----
WORKDIR /app

# ---- Copy project files ----
COPY pyproject.toml poetry.lock* /app/

# ---- Install dependencies ----
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# ---- Copy source code ----
COPY src /app/src
COPY tests /app/tests
COPY performance /app/performance

# ---- Install project package ----
RUN poetry install --no-interaction --no-ansi

# ---- Default command ----
CMD ["pytest", "-v"]