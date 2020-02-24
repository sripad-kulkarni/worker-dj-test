web: gunicorn project1.wsgi --log-file -
worker: celery worker --app=tasks.app
release: python config:set DOMAIN=$HEROKU_APP_URL.herokuapp.com
