FROM python:3.8.3  

WORKDIR /app

COPY ./requeriments.txt /

RUN pip install -r /requeriments.txt
