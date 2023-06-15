FROM python:3.10.4

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libopenblas-dev 

RUN apt-get clean

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .