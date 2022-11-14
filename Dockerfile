FROM python:3.10.4

ENV FLASK_APP=core

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY core /opt/core

WORKDIR /opt

CMD flask --app core run --host 0.0.0.0 -p $PORT
