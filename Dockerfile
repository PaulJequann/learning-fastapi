FROM python:3.9.7

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
