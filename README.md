# json-scheduler-example

Django JSON scheduler example project.

## Preconditions:

- Python 3.12
- PostgreSQL

## Clone the project

```
git clone https://github.com/avtavgen/json-scheduler.git
```

## Run local

### Setup virtual environment

```
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Create administrator

```
python manage.py createsuperuser
```

### Run server

```
python manage.py runserver
```

### Run tests

```
python manage.py test
```

## Run with docker

### Run server

```
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
```

### Run tests

```
docker-compose exec web python manage.py test
```

## API documentation

```
http://0.0.0.0/docs
```