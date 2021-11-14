release: python manage.py migrate
web: gunicorn smart_video_door_phone.wsgi --log-file -
daphne: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A smart_video_door_phone.celery worker -l info
celerybeat: celery -A smart_video_door_phone beat -l INFO
celeryworker2: celery -A smart_video_door_phone.celery worker & celery -A smart_video_door_phone beat -c 4 -l INFO & wait -n
