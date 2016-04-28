FROM centos:centos7
MAINTAINER Mohammed Zeeshan Ahmed <mohammed.zee1000@gmail.com>

EXPOSE 443

VOLUME /opt/certbox/certs
WORKDIR /opt/certbox

RUN yum install git -y && \
    yum install httpd -y && \
    yum install mod_ssl -y && \
    yum install epel-release -y && \
    yum install letsencrypt -y

ENV CERT_URL_LIST="test.com;www.test.com"
ENV CERT_ACTION="certonly"
ENV CERT_METH="--standalone"

COPY ./start.sh /opt/certbox/start.sh
COPY ./gencerts.py /opt/certbox/gencerts.py

ENTRYPOINT /opt/certbox/start.sh
