#!/bin/bash
DIR="$( cd "$( dirname "$0" )" && pwd )"
echo $DIR

cd $DIR

# ulimit -n 50000
nohup gunicorn --config=web2/gunicorn_conf.py web2.wsgi &> /dev/null &