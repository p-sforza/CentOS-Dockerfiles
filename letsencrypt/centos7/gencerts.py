#!/usr/bin/python

import os;
import sys;
from subprocess import call;

cert_urls = os.environ['CERT_URL_LIST']
cert_meth = os.environ['CERT_METH']

urls = cert_urls.split(";");

CMD = ["letsencrypt", "certonly", cert_meth, "--agree-tos", "--register-unsafely-without-email", "--dry-run"]

for url in urls:
    CMD.append("-d")
    CMD.append(url)

#CMD.append("/opt/certbox/certs/authfile")

call(CMD)
