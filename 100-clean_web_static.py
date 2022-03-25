#!/usr/bin/python3
""" Function that deploys """
from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


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


def deploy():
    """creates and distributes an archive to the web servers"""
    arch = do_pack()
    if arch is None:
        return False
    return do_deploy(arch)


def do_clean(number=0):
    """ remove archives """

    number = 1 if int(number) == 0 else int(number)

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
