FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /
RUN pip install -r /requirements.txt

COPY ./dockerfiles/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./dockerfiles/django/start-tests /start-tests
RUN sed -i 's/\r$//g' /start-tests
RUN chmod +x /start-tests

WORKDIR /app
