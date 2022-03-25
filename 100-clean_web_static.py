#!/usr/bin/python3
"""
Fabric script that generates archive
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


def do_clean(number=0):
    """Deletes out-of-date archives"""
    files = local("ls -1t versions", capture=True)
    file_names = files.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split("\n")
    for i in dir_server_names[n:]:
        if i is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(i))
