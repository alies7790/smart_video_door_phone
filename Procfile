release: python manage.py migrate
web: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
daphne: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
celeryworker2: celery -A smart_video_door_phone.celery  worker  -c 4 & celery -A smart_video_door_phone beat -l INFO & wait -n



worker: python manage.py runworker channels  --settings=smart_video_door_phone.settings -v2