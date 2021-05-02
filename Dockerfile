FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && apk add zlib-dev jpeg-dev gcc musl-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/

