FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

# ---- Install uv ----
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# ---- Workdir ----
WORKDIR /app

# Copy dependency files first (layer caching)
COPY pyproject.toml uv.lock /app/

# Install dependencies (without project yet)
RUN uv sync --frozen --no-install-project

# Copy full project
COPY . /app

# Install project package itself
RUN uv sync --frozen

CMD ["uv", "run", "pytest", "-v", "--alluredir=allure-results"]