#!/bin/bash

source .env  > /dev/null 2>&1

docker-compose down

if [[ $STATE == *"DEV"* ]]; then
    # запускаем асинхронность только для разработки
    docker-compose up --build
else
    # на production слабый сервер. можно будет быстро
    # поодключить асинхронность при необходимости
    docker-compose up --build --no-start
    docker-compose start mysql web nginx certbot
fi
