#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


def do_clean(number=0):
    """remove archive"""
    number = int(number)
    if number == 0 or number == 1:
        local("cd versions && ls -C1 -t| awk 'NR>1'|xargs rm -rf")
        run("cd /data/web_static/releases && ls -C1 -t| awk \
            'NR>1'|xargs rm -rf")
    else:
        local("cd versions && ls -C1 -t| awk \
            'NR>{}'|xargs rm -rf".formta(number))
        run("cd /data/web_static/releases && ls -C1 -t| awk \
            'NR>{}'|xargs rm -rf".formta(number))
