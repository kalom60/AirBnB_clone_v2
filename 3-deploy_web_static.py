#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env

env.hosts = [
    'ubuntu@35.227.37.173',
    'ubuntu@18.207.135.118'
]


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """creates and distributes an archive to the web servers"""
    try:
        packed = do_pack()
    except Exception:
        return False

    return do_deploy(packed)
