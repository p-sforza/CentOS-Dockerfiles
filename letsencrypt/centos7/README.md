# Dockerfiles-centos-letsencrypt
Centos dockerfile for letsencrypt

Tested on docker 1.9.1 on centos 7 atomic host.

## Building : 

Copy/clone the sources to your system and get into the directory.

 $ docker build -t [yourname]/letsencrypt .

## Usage : 

 $ docker run [-e env1=val1 -e env2=val2] -v  /path/todir:/opt/certbox/certs [yourname]/letsencrypt
 
###Environment Variables and their purpose : 

 1. LETSENCRYPT_URLS - The semicolon separated list of urls on which the certificates will be generated. Example : LETSENCRYPT_URLS="test.com;www.test.com" = -d test.com -d www.test.com
 2. LETSENCRYPT_COMMAND - The letsencrypt command to be run. Values include 'certonly', 'renew', 'run', 'revoke', 'rollback' and so on.
 3. LETSENCRYPT_METHOD - The name of the plugin to use to generate the certs. Values include '--manual', '--standalone' and '--webroot'. Webroot is currently a work in progress however.
 4. LETSENCRYPT_DRYRUN - If, true, then --dry-run is appended to the letsencrypt command.
 5. LETSENCRYPT_NOEMAIL -If true, then unsafe registration is done.
