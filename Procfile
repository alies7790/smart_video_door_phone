release: python manage.py migrate
web1: gunicorn smart_video_door_phone.wsgi --log-file -
worker: python manage.py runworker channels -v2
web2: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
web: gunicorn smart_video_door_phone.asgi:application -k uvicorn.workers.UvicornWorker
daphne: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
celeryworker2: celery -A smart_video_door_phone.celery  worker  -c 4 & celery -A smart_video_door_phone beat -l INFO & wait -n
