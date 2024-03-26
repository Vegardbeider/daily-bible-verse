FROM python:3.10-alpine3.19

COPY app app

RUN pip install -r /app/requirements.txt

RUN crontab /app/crontab

CMD [ "crond", "-f" ]