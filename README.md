# todo-python-api

This is a todoAPI using Python, Django, SQLite and Docker

## 1. Use the IDE to jump into a python venv

Running this project in a python venv and use pip to install our deps.

```console
python -m venv venv
.\venv\Scripts\activate // for windows
source venv/bin/activate // for mac
pip install -r requirements.txt
```

Run Migrations

```console
python manage.py makemigrations
python manage.py migrate
```

Run the server

```console
python manage.py runserver
```

Create superuser

```console
python manage.py createsuperuser
```

To jump out of our venv and back to our host machine.

```console
deactivate
```

## 2. Use Docker compose

Use `docker-compose.yml`

```console
docker-compose up --build
docker-compose down
```

To check the status of your Docker container

```console
docker container ls
```

Run migrations

```console
docker-compose run web python manage.py migrate
```

## 3. Access Your Application

Once the container is up and running, you can access your Django application at http://localhost:8000.

Access Swagger UI

Open your browser and navigate to http://localhost:8000/swagger/ to view the Swagger UI. You should see your API endpoints documented and available for testing.

Alternatively, you can view the ReDoc documentation at http://localhost:8000/redoc/.

## Other commands for cleaning up

```console
docker rm container_name
docker image rm image_name
docker system prune
docker images prune
```

Check folder size:

```console
du -sh *
```
