#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that send an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        arch = archive_path.split("/")[-1]
        f_name = arch.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, f_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arch, path, f_name))
        run('rm /tmp/{}'.format(arch))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, f_name))
        run('rm -rf {}{}/web_static'.format(path, f_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, f_name))
        return True
    except:
        return False
