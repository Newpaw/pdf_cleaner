FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y poppler-utils && \
    pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
