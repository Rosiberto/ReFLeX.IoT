FROM python:3.9.18-alpine

WORKDIR /server/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .