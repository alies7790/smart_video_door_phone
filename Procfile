web: gunicorn smart_video_door_phone.wsgi --log-file -
web2: daphne smart_video_door_phone.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=smart_video_door_phone.settings -v2