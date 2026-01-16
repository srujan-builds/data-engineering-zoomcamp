FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ingestion_pipeline.py .

CMD ["python", "ingestion_pipeline.py"]