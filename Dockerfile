FROM python:3.12.1-slim-bullseye

RUN apt-get update && apt-get install -y curl
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && rm ./requirements.txt