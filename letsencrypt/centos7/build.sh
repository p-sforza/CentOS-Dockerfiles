#!/usr/bin/env bash

imgname="mohammedzee1000/letsencrypt";

docker build -t ${imgname} .
docker push ${imgname};
