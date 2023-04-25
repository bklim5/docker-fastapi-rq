FROM python:3.9.16

COPY app /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
