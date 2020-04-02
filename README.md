# Django Training

### Deploy for end user
 1. Clone to your local machine: `git clone https://github.com/maierraul96/django-training.git`
 2. Create an image from Dokerfile:
    `docker build -t counter .`
 3. Run image: `docker run -p 8000:8000 --env-file .\.env.dev counter`
 4. Access app at `localhost:8000`
 
 ### Deploy for site admins
 1. Clone to your local machine: `git clone https://github.com/maierraul96/django-training.git`
 2. Create an image from Dokerfile:
    `docker build -t counter .`
 3. Run image: `docker run -p 8000:8000 --env-file .\.env.dev counter`
 4. Open an interactive shell into container: `docker exec -it <CONTAINER_ID> sh`
 5. Create superuser: `python django_training/manage.py createsuperuser`
 4. Access app at `localhost:8000/admin`
 
 ### Deploy for developers (Windows)
  - Clone to your local machine: `git clone https://github.com/maierraul96/django-training.git`
  - Activate virtual environment: `venv\Scripts\activate`
  - Add following environment variables to your virtual env: 
 ```
set DEBUG=1
set SECRET_KEY="ouo95ae066(+yz-whm$&l@=2$iblla)69)rcp#brlt$8*hcuki"
set DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
set DJANGO_SETTINGS_MODULE=django_training.settings
```
  - Change directory to "django_project": `cd django_project`
  - Configure DB in `django_project/django_training/settings.py`
  - Apply migrations: `py manage.py migrate`
  - Make changes to code
  - Run tests: `py manage.py test`
  - Run server: `py amange.py runserver 8000`