FROM ubuntu:16.04

RUN /usr/bin/apt-get update -q && \
    /usr/bin/apt-get install -qqy build-essential git && \
    /usr/bin/apt-get install -qqy python-pip python-dev && \
    /usr/bin/apt-get install -qqy uwsgi uwsgi-plugin-python && \
    /usr/bin/apt-get clean && \
    /bin/rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY /web-app.ini /etc/uwsgi/apps-enabled/

RUN /bin/mkdir /opt/web-app && \
    cd /opt/web-app && \
    /usr/bin/git clone https://github.com/brysontyrrell/Jackalope.git /opt/web-app && \
    /usr/bin/pip install -r requirements.txt && \
    /bin/chown -R www-data:www-data /opt/web-app

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ENV DATABASE_NAME ${MYSQL_DATABASE}
ENV DATABASE_USER ${MYSQL_USER}
ENV DATABASE_PASSWD ${MYSQL_PASSWORD}

CMD ["uwsgi", "--ini", "/etc/uwsgi/apps-enabled/web-app.ini"]
