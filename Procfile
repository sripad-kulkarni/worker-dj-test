web: gunicorn project1.wsgi --log-file -
worker: celery worker --app=tasks.app
release: python manage.py migrate
