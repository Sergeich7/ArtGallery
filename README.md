# ArtGallery
artgallery-tatyana.ru - Художественная галерея. При разработки использовал Python, Django framework, Django REST framework, MySQL. REST API используется для получения данных о картинах телеграмм-ботом. Арт-объекты можно просматривать по категориям. Аутентифицированные пользователи могут добавлять/удалять комментарии.

Описание REST API

Возвращается все данные сущьности
https://artgallery-tatyana.ru/api/cats/
https://artgallery-tatyana.ru/api/techs/
https://artgallery-tatyana.ru/api/auths/
https://artgallery-tatyana.ru/api/prods/

Возвращается конкрентная запись
https://artgallery-tatyana.ru/api/prods/4/
https://artgallery-tatyana.ru/api/cats/3/
https://artgallery-tatyana.ru/api/techs/2/
https://artgallery-tatyana.ru/api/auths/1/

Возвращает список продуктов в зависимости о фильтра.
Фильтры можно задавать в люьом порядке. Или вообще не задавать
https://artgallery-tatyana.ru/api/filter/author/1/category/2/technique/4/
