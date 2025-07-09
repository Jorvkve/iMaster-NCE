FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]