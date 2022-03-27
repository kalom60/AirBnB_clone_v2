#!/usr/bin/python3
""" Function that deploys """
from fabric.api import run, env, local

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


def do_clean(number=0):
    """remove archive"""
    if int(number) >= 2:
        local("cd versions/ && rm $(ls -t | awk 'NR>{}')".format(number))
        run("cd /data/web_static/releases && rm -rf $(ls -t | awk 'NR>{}')"
            .format(number))
    elif int(number) == 1 or int(number) == 0:
        local("cd versions/ && rm $(ls -t | awk 'NR>1')")
        run("cd /data/web_static/releases && rm -rf $(ls -t | awk 'NR>1')")
