FROM centos:centos7
MAINTAINER Mohammed Zeeshan Ahmed <mohammed.zee1000@gmail.com>

EXPOSE 443

VOLUME /opt/certbox/certs
WORKDIR /opt/certbox/certs

RUN yum install git -y && \
    yum install httpd -y && \
    yum install mod_ssl -y && \
    yum install epel-release -y && \
    yum install letsencrypt -y

ENV LETSENCRYPT_URLS="test.com;www.test.com"
ENV LETSENCRYPT_COMMAND="certonly"
ENV LETSENCRYPT_METHOD="--manual"
ENV LETSENCRYPT_DRYRUN="true"
ENV LETSENCRYPT_NOEMAIL="true"

COPY ./start.sh /opt/certbox/start.sh
COPY ./gencerts.py /opt/certbox/gencerts.py

ENTRYPOINT /opt/certbox/start.sh
