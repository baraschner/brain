FROM python:3.8-slim-buster

RUN pip install -U pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/wait-for-it.sh .
RUN chmod 755 wait-for-it.sh

COPY ./brain /brain
