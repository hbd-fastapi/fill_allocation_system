FROM python:3.9-slim-buster

ENV WORKDIR='/app'

ENV PYTHONDONTWRITEBYTECODE 1

# To log changes
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
    && apt-get clean

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/