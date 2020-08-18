#!/usr/bin/python3
"""
distribute it awsome code
"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os
env.hosts = ['1604-web-01', '1604-web-02']


def do_deploy(archive_path):
    """
    Function that generate a .tgz
    """
    if os.path.isfile(archive_path) is False:
        return False
    archive = archive_path.split("/")[-1]
    path = "/data/web_static/releases"
    put("{}".format(archive_path), "/tmp/{}".format(archive))
    folder = arhive.split(".")
    run("mkdir -p {}/{}/".format(path, folder[0]))
    new_archive = '.'.join(folder)
    run("tar -xzf /tmp{} -C {}/{}/"
        .format(new_archive, path, folder[0]))
    run("rm /tmp/{}".format(archive))
    run("mv {}/{}/web_static/* {}/{}/"
        .format(path, folder[0], path, folder[0]))
    run("rm -rf {}/{}/web_static".format(path, folder[0]))
    run("rm -rf /data/web_static/current")
    run("ln -sf {}/{} /data/web_static/current"
        .format(path, folder[0]))
    print("New versión deployed!")
    return true
except:
    return False
