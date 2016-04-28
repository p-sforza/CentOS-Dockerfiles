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

ENV CERT_URL="test.com"
ENV CERT_METH="standalone"

RUN alias certgen="letsencrypt certonly --agree-tos --register-unsafely-without-email"

COPY ./gencert.sh /opt/certbox/gencert.sh

ENTRYPOINT /opt/certbox/gencert.sh