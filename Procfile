web: gunicorn project1.wsgi --log-file -
worker: celery worker --app=tasks.app
release: heroku config:set DOMAIN=$HEROKU_APP_URL.herokuapp.com
