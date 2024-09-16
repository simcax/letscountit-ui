FROM python:3.12 AS builder
LABEL maintainer="carsten@skov.codes"
RUN apt update
RUN apt install -y gunicorn3 
WORKDIR /app
RUN python3 -m pip install --upgrade pip poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml poetry.lock ./
RUN poetry install
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/.venv .venv/
ENV FLASK_APP=letscountit
ENV VIRTUAL_ENV=/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY ./letscountitui letscountitui/
COPY ./docker/config config
COPY ./docker/docker_entrypoint.sh .
RUN chmod +x docker_entrypoint.sh
WORKDIR /app
EXPOSE 8000

ENTRYPOINT [ "./docker_entrypoint.sh" ]
CMD [ "/app/.venv/bin/gunicorn", "-c", "python:config.gunicorn", "letscountitui.app:app" ]