FROM python:3.11-slim AS base

WORKDIR /app

# RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM base AS dev
ENV FLASK_APP=backend.py
ENV FLASK_DEBUG=1
CMD ["flask", "run", "--host=0.0.0.0"]

FROM base AS production-stage
ARG WORKER=1
ENV FLASK_DEBUG=0
EXPOSE 5000
CMD ["gunicorn", "-w", "${WORKER}", "-b", "0.0.0.0:5000", "backend:app"]