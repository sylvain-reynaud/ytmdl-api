FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# From https://github.com/docker-library/golang
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  ffmpeg \
  tzdata \
  gcc \
  libc-dev \
  make \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app