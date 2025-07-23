FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Set environment variables to reduce memory usage
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_COMPILE_BYTECODE=1
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/gcp-key.json

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies with minimal footprint
RUN uv sync --frozen --no-cache --no-dev && \
    # Clean up package cache
    rm -rf ~/.cache/uv && \
    # Remove pip cache
    python -m pip cache purge 2>/dev/null || true

# Copy application code (.dockerignore excludes .venv)
COPY . .

# Create non-root user for security and potentially lower memory usage
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Expose port
EXPOSE 8080

# Run the application with memory-optimized Python settings
CMD ["uv", "run", "python", "-O", "-m", "app"]