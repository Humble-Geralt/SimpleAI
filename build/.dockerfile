FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

EXPOSE 5000

CMD ["gunicorn", "--config", ".\gunicorn\gunicorn_config.py", "app:app"]