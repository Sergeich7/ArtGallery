FROM python:3.9-slim
LABEL maintainer="Vitaly Belashov pl3@yandex.ru"
RUN apt-get update
RUN apt-get -y install git default-libmysqlclient-dev
RUN apt-get -y install git build-essential
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt start.sh /app/
RUN pip install -r requirements.txt
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
#CMD ["ls"]
#CMD ["python manage.py runserver 0.0.0.0:8000"]
CMD ["./start.sh"]


