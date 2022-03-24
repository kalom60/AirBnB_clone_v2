#!/usr/bin/python3
"""This script will distribute archive in webserver"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """depoly archives"""
    if exists(archive_path) is False:
        return False
    else:
        try:
            file = archive_path.split('/')[1]
            arch = file.split(".")[0]
            put(archive_path, "/tmp/")
            run("mkdir -p /data/web_static/releases/{}/".format(arch))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(file, arch))
            run("rm /tmp/{}".format(file))
            run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(arch, arch))
            run("rm -rf /data/web_static/releases/{}/web_static/".format(arch))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(arch))
            return True
        except:
            return False
