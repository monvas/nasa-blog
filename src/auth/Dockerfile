FROM python:3.9

# Install pkg-config
RUN apt-get update && \
    apt-get install -y pkg-config

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests build-essential libpq-dev python3-dev && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5001

CMD ["python", "main.py"]