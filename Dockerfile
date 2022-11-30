FROM python:3.9-slim
LABEL maintainer="Vitaly Belashov pl3@yandex.ru"
RUN apt-get update
#RUN apt-get -y install python3-dev
RUN apt-get -y install git default-libmysqlclient-dev
RUN apt-get -y install git build-essential
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt start.sh /app/
RUN pip install -r requirements.txt
RUN chmod +x start.sh
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
CMD ["./start.sh"]


