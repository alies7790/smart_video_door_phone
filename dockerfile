FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
RUN mkdir /code/static
RUN heroku config:set DISABLE_COLLECTSTATIC=1
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
