#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *
import os

env.hosts = [
    '35.227.37.173',
    '18.207.135.118'
]
env.user = "ubuntu"


def do_clean(number=0):
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
