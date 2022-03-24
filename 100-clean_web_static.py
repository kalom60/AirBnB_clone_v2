#!/usr/bin/python3
""" Function that deploys """
from fabric.api import local, run, env
from os.path import exists


env.hosts = ['35.231.33.237', '34.74.155.163']
env.user = "ubuntu"


def do_clean(number=0):
    """ remove archive """

    if exists('versions'):
        if int(number) == 0:
            num = 2
        else:
            num = int(number) + 1
        cmd = 'tail -n +{}| xargs rm -rf'.format(num)
        local('cd versions ; ls -t|{}'.format(cmd))
        path = '/data/web_static/releases'
        run('cd {}; ls -t| grep web_static|{}'.format(path, cmd))
