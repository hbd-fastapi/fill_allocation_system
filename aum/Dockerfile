FROM python:3.9-slim-buster
ENV WORKDIR='/code'

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
    && apt-get clean

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "-u", "server.py"]