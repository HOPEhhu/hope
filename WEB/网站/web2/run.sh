#!/bin/bash
DIR="$( cd "$( dirname "$0" )" && pwd )"
echo $DIR

cd $DIR

# ulimit -n 50000

#nohup:不挂断的运行命令，--config: 修改指定的配置文件
nohup gunicorn --config=web2/gunicorn_conf.py web2.wsgi &> /dev/null &