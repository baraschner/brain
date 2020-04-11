FROM python:3.8-slim-buster
COPY ./brain /brain
COPY requirements.txt .
COPY scripts/wait-for.sh .

RUN pip install -r requirements.txt
RUN chmod 755 wait-for.sh

