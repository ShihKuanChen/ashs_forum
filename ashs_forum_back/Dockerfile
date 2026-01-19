FROM python:3.11-slim

WORKDIR /app

ENV FLASK_APP=backend.py
ENV FLASK_DEBUG=1

# RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]