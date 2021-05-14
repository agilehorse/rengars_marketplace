FROM python:3.9.4-alpine

LABEL MAINTAINER="Dávid Michal Bulko dmbulko@gmail.com"
ARG MARKETPLACE_PORT

ENV GROUP_ID=1000 \
    USER_ID=1000 \
    GUNICORN_CMD_ARGS="-w=4 --bind=0.0.0.0:${MARKETPLACE_PORT}"

WORKDIR /var/www/

ADD . /var/www/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
RUN pip install connexion[swagger-ui]

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh
USER www

EXPOSE ${MARKETPLACE_PORT}

CMD ["gunicorn", "App"]