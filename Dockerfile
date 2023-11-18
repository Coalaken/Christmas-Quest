FROM python:3.10-alpine

WORKDIR /usr/src/

COPY req.txt .

RUN pip install --upgrade pip

RUN pip install -r req.txt

