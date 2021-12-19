#!/bin/bash
# You need permissions to run this!

sudo mkdir CVE-2019-18277
sudo chown $(id -u):$(id -g) CVE-2019-18277

cat <<EOF > CVE-2019-18277/docker-compose.yml
version: '3.7'
services:
  web:
    image: mosesrenegade/cve-2019-18277-web
    command: gunicorn --keep-alive 10 -k gevent --bind 0.0.0.0:6767 -w 4 backend:app
    ports:
      - 6767:6767
  haproxy:
    image: mosesrenegade/cve-2019-18277-ha
    container_name: http.sec642.org
    ports:
      - 1080:1080
EOF
