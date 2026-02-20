FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3

# ---- Install Poetry ----
RUN pip install "poetry==$POETRY_VERSION"

# ---- Workdir ----
WORKDIR /app

# Copy dependency files first (layer caching)
COPY pyproject.toml poetry.lock* /app/

# Disable virtualenv inside container
RUN poetry config virtualenvs.create false

# Install dependencies (without project yet)
RUN poetry install --no-interaction --no-ansi

# Copy full project
COPY . /app

# Install project package itself
RUN poetry install --no-interaction --no-ansi

CMD ["pytest", "-v"]