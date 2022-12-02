#!/bin/bash

source .env  > /dev/null 2>&1

docker-compose down
docker-compose up --build --no-start

docker-compose start mysql web nginx certbot

if [[ $STATE == *"DEV"* ]]; then
    # запускаем асинхронность только для разработки
    # на production - слабый сервер
    # можно будет быстро поодключить при необходимости
    docker-compose start rabbit redis celery flower phpmyadmin
fi
