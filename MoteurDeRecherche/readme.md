# MySerach Engine

Require :

- docker 
- docker-compose

Start Project 

```
docker-compose up
```

Load data

```
docker-compose run --rm web python manage.py migrate

docker-compose run --rm web python manage.py refreshOnSaleList
docker-compose run --rm web python manage.py refreshAvailableList
docker-compose run --rm web python manage.py refreshImageList
```