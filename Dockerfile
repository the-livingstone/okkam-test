FROM python:3.11-alpine as builder

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED=1 \
    PATH=/root/.local/bin:$PATH

# FIXME: for m1 (arm64)
RUN apk add gcc
RUN apk add musl-dev
RUN apk add libffi-dev

RUN pip3 install --upgrade pip poetry

COPY . .

RUN poetry config virtualenvs.in-project true
RUN poetry install --only main --no-interaction --no-ansi


FROM python:3.11-alpine as production
WORKDIR /usr/src/app/

COPY --from=builder /usr/src/app/.venv /usr/src/app/.venv
COPY --from=builder /usr/src/app/app /usr/src/app/app
COPY --from=builder /usr/src/app/startup.py /usr/src/app/startup.py

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/usr/src/app/.venv/bin:$PATH

FROM builder as test

RUN poetry install --no-root  --no-interaction --no-ansi