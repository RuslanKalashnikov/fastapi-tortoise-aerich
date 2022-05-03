FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/toerich
COPY requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .
