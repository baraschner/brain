FROM python:3.8-slim-buster

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/wait-for.sh .
RUN chmod 755 wait-for.sh

COPY ./brain /brain
