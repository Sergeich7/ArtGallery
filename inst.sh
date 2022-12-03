#!/bin/bash

source .env  > /dev/null 2>&1

docker-compose down
docker-compose up --build --no-start

if [[ $STATE == *"DEV"* ]]; then
    # запускаем асинхронность только для разработки
    docker-compose up
else
    # на production слабый сервер. можно будет быстро
    # поодключить асинхронность при необходимости
    docker-compose start mysql web nginx certbot
fi
