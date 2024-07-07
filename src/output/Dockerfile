FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install poetry
RUN poetry install --no-root

ENV PYTHONPATH="/app"

ENTRYPOINT ["poetry", "run", "python", "src/output/output.py"]