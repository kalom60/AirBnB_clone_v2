#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
       distributes an archive to your web servers
Returns False if the file at the path archive_path doesn't exist
"""
from os.path import isdir, isfile
from fabric.api import *
from fabric.operations import run, put, sudo
from datetime import datetime
env.hosts = ['35.227.37.173', '18.207.135.118']


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
    """ script that distributes archive to web servers
    All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
    Returns True if all operations has been done correctly,
            otherwise returns False
    """
    if (isfile(archive_path) is False):
        return False

    try:
        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/")
        unpack = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + unpack.split(".")[0])
        run("sudo mkdir -p {:s}".format(folder))
        run("sudo tar -xzf /tmp/{:s} -C {:s}".format(unpack, folder))
        run("sudo rm /tmp/{:s}".format(unpack))
        run("sudo mv {:s}/web_static/* {:s}/".format(folder, folder))
        run("sudo rm -rf {:s}/web_static".format(folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {:s} /data/web_static/current".format(folder))
        return True
    except:
        return False



def deploy():
    """Deploy"""
    try:
        archive_path = do_pack()
        deployed = do_deploy(archive_path)
        return deployed
    except:
        return False
