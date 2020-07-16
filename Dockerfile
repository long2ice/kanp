FROM python:3
RUN mkdir -p /kanp
WORKDIR /kanp
COPY pyproject.toml poetry.lock /kanp/
RUN pip3 install poetry
ENV POETRY_VIRTUALENVS_CREATE false
RUN poetry install --no-root
COPY . /kanp
RUN poetry install
CMD ["kanp","serve"]