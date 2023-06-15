FROM python:3.8
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libopenblas-dev \
    libomp-dev

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt