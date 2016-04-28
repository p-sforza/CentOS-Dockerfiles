#!/usr/bin/env bash

#logfile="/opt/certbox/certs/log";
alias certgen="letsencrypt certonly --agree-tos --register-unsafely-without-email"


#case ${CERT_METH} in
#    webroot)
#        certgen --dryrun --webroot -w /opt/letsencrypt/certs/ -d  ${CERT_URL}  > ${logfile};
#    ;;
#    standalone)
#        certgen --dryrun --stanalone -d ${CERT_URL} > ${logfile};
#    ;;
#    *)
#        echo "Invalid method specified, exiting ..." > ${logfile} ;
#    ;;
#esac

/opt/certbox/gencerts.py;

