# Use Python 3.10 slim base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for building some Python packages
RUN apt-get update && apt-get install -y \
    build-essential gcc g++ libffi-dev libssl-dev python3-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy Poetry config files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies without creating a virtual environment inside container
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy application source code
COPY . /app

# Optional: download spaCy models here only if not installed via Poetry dependencies
# RUN poetry run python -m spacy download en_core_web_sm && \
#     poetry run python -m spacy download pt_core_news_sm

# Run your bot using Poetry-managed environment
CMD ["poetry", "run", "python", "src/telegram_bot.py"]