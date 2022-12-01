FROM python:3.10-slim
LABEL maintainer="Vitaly Belashov pl3@yandex.ru"
RUN apt-get update
RUN apt-get -y install git python3-dev
RUN apt-get -y install git default-libmysqlclient-dev
RUN apt-get -y install git libssl-dev
RUN apt-get -y install git build-essential
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8000
ENV PYTHONUNBUFFERED 1


