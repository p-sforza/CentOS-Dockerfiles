#!/usr/bin/python

import os;
import sys;
from subprocess import call;

letsencrypt_urls = os.environ['LETSENCRYPT_URLS']
letsencrypt_meth = os.environ['LETSENCRYPT_METHOD']
letsencrypt_cmd = os.environ['LETSENCRYPT_COMMAND']
letsencrypt_dryrun = os.environ['LETSENCRYPT_DRYRUN']
letsencrypt_noemail = os.environ['LETSENCRYPT_NOEMAIL']


urls = letsencrypt_urls.split(";");

CMD = ["letsencrypt", letsencrypt_cmd, letsencrypt_meth, "--agree-tos"]

if letsencrypt_dryrun == "true":
    CMD.append("--dry-run")

if letsencrypt_noemail == "true":
    CMD.append("--register-unsafely-without-email")

for url in urls:
    CMD.append("-d")
    CMD.append(url)

#CMD.append("/opt/certbox/certs/authfile")

call(CMD)
