#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = 'ubuntu'


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local('mkdir versions')
        arch_path = "versions/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static'.format(arch_path))
        return arch_path
    except Exception:
        return None


def do_deploy(archive_path):
    """send archive to web server"""
    if exists(archive_path) is False:
        return False

    try:
        file = archive_path.split('/')[1]
        file_name = file.split('.')[0]
        print(file_name)
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, file_name))
        run('rm -rf /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, file_name))
        run('rm -rf {}{}/web_static'.format(path, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_name))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    try:
        archive_path = do_pack()
    except Exception:
        return False

    return do_deploy(archive_path)
