FROM ubuntu:22.04

RUN apt update -y \
    && apt upgrade -y \
    && apt install nano apache2 curl -y

RUN echo 'Hello, World!' > index.html

WORKDIR /usr/local/apache2/htdocs/

RUN cp /index.html .

CMD /usr/sbin/apache2ctl -D FOREGROUND