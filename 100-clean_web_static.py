#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *
from os.path import exists

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


def do_clean(number=0):
    """remove archive"""
    if exists('versions'):
        if int(number) == 0:
            num = 1
        else:
            num = int(number)
        command = 'tail -n +{}| xargs rm -rf'.format(num)
        local('cd versions ; ls -t|{}'.format(command))
        dir = '/data/web_static/releases'
        run('cd {}; ls -t| grep web_static|{}'.format(dir, command))
