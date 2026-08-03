FROM python:3.11-slim

WORKDIR /app

COPY app.py ./
RUN pip install --no-cache-dir redis

CMD ["python", "app.py"]
