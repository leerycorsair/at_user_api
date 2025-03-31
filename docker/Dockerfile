FROM python:3.12-slim

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock / 
RUN poetry install --no-root

COPY . .

CMD ["poetry", "run", "python", "-m"  "at_user_api"]
