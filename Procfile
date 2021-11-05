web: gunicorn smart_video_door_phone.wsgi --log-file -
web2: daphne smart_video_door_phone.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2


