FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

# From https://github.com/docker-library/golang
RUN apk --no-cache add \
  ffmpeg \
  tzdata \
  gcc \
  libc-dev \
  make

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80