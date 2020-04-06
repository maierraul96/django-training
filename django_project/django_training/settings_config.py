import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
SECRET_KEY = "ouo95ae066(+yz-whm$&l@=2$iblla)69)rcp#brlt$8*hcuki"
DJANGO_ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
DJANGO_SETTINGS_MODULE = "django_training.settings"

SQL_ENGINE = "django.db.backends.postgresql"
SQL_DATABASE = "counter_app"
SQL_USER = "postgres"
SQL_PASSWORD = "postgresadmin"
SQL_HOST = "db"
SQL_PORT = "5432"
DATABASE = "postgres"


# SQL_ENGINE = "django.db.backends.sqlite3"
# SQL_DATABASE = os.path.join(BASE_DIR, "db.sqlite3")
# SQL_USER = "user"
# SQL_PASSWORD = "password"
# SQL_HOST = "localhost"
# SQL_PORT = "5432"

if __name__ == '__main__':
    os.environ["SQL_HOST"] = SQL_HOST
    os.environ["SQL_PORT"] = SQL_PORT
