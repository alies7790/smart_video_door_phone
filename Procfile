
web: gunicorn --pythonpath smart_video_door_phone smart_video_door_phone.deploy --log-file -
daphne: daphne smart_video_door_phone.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2

