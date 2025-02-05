FROM python:3.9-slim
RUN apt-get update
RUN pip install --upgrade pip
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD python main.py
