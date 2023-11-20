FROM python:3.10-alpine

WORKDIR /usr/src/

EXPOSE 8000

COPY req.txt .

RUN pip install --upgrade pip

RUN pip install -r req.txt

COPY backend/ .
