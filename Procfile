release: python manage.py migrate
daphne: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
celeryworker2: celery -A smart_video_door_phone.celery  worker  -c 4 & celery -A smart_video_door_phone beat -l INFO & wait -n


web1: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=smart_video_door_phone.settings -v2