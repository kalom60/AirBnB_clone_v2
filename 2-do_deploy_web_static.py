#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """send archive to web server"""
    if exists(archive_path):
        try:
            file = archive_path.split('/')[1]
            file_name = file.split(".")[0]
            path = "{}"
            put(archive_path, "/tmp/")
            run("mkdir -p {}{}/".format(path, file_name))
            run("tar -xzf /tmp/{} -C {}{}/"
                .format(file, path, file_name))
            run("rm /tmp/{}".format(file))
            run("mv {0}{1}/web_static/* \
                {0}{1}/".format(path, file_name))
            run("rm -rf {}{}/web_static/".format(path, file_name))
            run("rm -rf /data/web_static/current")
            run("ln -s {}{}/ /data/web_static/current"
                .format(path, file_name))
        except:
            return False
    else:
        return False
