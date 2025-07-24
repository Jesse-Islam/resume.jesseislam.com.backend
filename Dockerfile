# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# use ASCII hyphens here:
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8080
ENV PORT 8080
CMD ["sh","-c","exec gunicorn --bind 0.0.0.0:$PORT main:app"]
