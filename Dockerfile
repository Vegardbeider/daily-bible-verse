FROM python:3.9.18-alpine3.18

COPY app app

RUN crontab /app/crontab

CMD [ "crond", "-f" ]