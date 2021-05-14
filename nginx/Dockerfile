FROM alpine:latest

LABEL MAINTAINER="Dávid Michal Bulko dmbulko@gmail.com"
ARG BUILD_TYPE

RUN apk --update add nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir /etc/nginx/sites-enabled/ && \
    mkdir -p /run/nginx && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf /var/cache/apk/*

COPY conf.d/app.${BUILD_TYPE}.conf /etc/nginx/conf.d/app.conf

EXPOSE 81 444

CMD ["nginx", "-g", "daemon off;"]