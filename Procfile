
web: gunicorn --pythonpath social-team-builder social_team_builder.deploy --log-file -
daphne: daphne social_team_builder.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2

