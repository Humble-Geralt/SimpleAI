FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--config", "./gunicorn/gunicorn_config.py", "app:app"]
