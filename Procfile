web: gunicorn project1.wsgi --log-file -
release: python manage.py migrate
worker: celery worker --app=tasks.app