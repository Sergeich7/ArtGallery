FROM python:3.9-slim
RUN apt-get update
#RUN apt-get -y install python3-dev
RUN apt-get -y install git default-libmysqlclient-dev
RUN apt-get -y install git build-essential
WORKDIR /app
COPY requirements.txt start.sh /app/
RUN pip install -r  requirements.txt
#COPY . /app
RUN chmod +x start.sh
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
CMD ["./start.sh"]


