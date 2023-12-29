FROM python:3.12.1-bullseye

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && rm ./requirements.txt
