FROM python:3.12-slim-bookworm

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG en_US.UTF-8

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        build-essential \
        libpq-dev \
        vim \
        postgresql-client


# Install Odoo
RUN adduser --disabled-password --home /opt/flask --gecos '' flask
RUN pip3 install --upgrade pip
RUN pip3 install waitress

# Expose Odoo services
EXPOSE 8080

USER flask

WORKDIR /opt/flask

COPY . .

RUN pip3 install -r requirements.txt

CMD ["waitress-serve", "--call", "flaskr:create_app"]