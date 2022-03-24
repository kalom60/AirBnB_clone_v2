#!/usr/bin/python3
"""This script will distribute archive in webserver"""

from fabric.api import *
from fabric.operations import run, put
import os

env.hosts = [
    'ubuntu@35.227.37.173',
    'ubuntu@18.207.135.118'
]


def do_deploy(archive_path):
    """This function will depoly archives"""
    if not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split('/')[1]
        arch = file.split(".")[0]
        path = '/data/web_static/releases/'
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, arch))
        run("tar -xzf /tmp/{} -C {}{}/"
            .format(file, path, arch))
        run("rm /tmp/{}".format(file))
        run("mv {}{}/web_static/* \
            {}{}/".format(path, arch, path, arch))
        run("rm -rf {}{}/web_static/".format(path, arch))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current"
            .format(path, arch))
        return True
    except:
        return False
