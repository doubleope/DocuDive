FROM python:3.10.4

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    nginx \
    cmake \
    libopenblas-dev 

RUN apt-get clean

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY sagemaker /opt/program
COPY src /opt/program
COPY .env .

RUN chmod +x /opt/program

WORKDIR /opt/program

RUN python ingest.py