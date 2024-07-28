FROM python:3.11.5
# ENV PYTHONUNBUFFERED=1
WORKDIR /code/

# Use modern Poetry installer here
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry install

COPY . /code
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:8000", "--workers=5", "app.wsgi" ]
