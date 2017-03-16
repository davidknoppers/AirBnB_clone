#!/usr/bin/python3
"""
distributes an archive to our web servers
we are learning how to properly manage code deployment
with tar and fabric
"""
from fabric.api import *
import sys
import time


env.hosts = ['52.90.159.84', '54.242.30.104']


def do_pack():
    """ tarballs web_static"""
    path = "web_static_{:s}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static/".format(path))
    except:
        return None


def do_deploy(archive_path):
    """
    uploads tarball
    unpacks tarball
    cleans up directories
    """
    try:
        put(archive_path, "/tmp/")
        path = archive_path.strip("versions/")
        directory = "/data/web_static/releases/"
        temp = "sudo mkdir -p " + directory + path
        run(temp)
        temp = "sudo tar -xzf /tmp/" + path + " -C " + directory + path
        run(temp)
        temp = "sudo rm /tmp/" + path
        run(temp)
        temp = "sudo mv " + directory + path
        temp += "/web_static/* " + directory + path + "/"
        run(temp)
        temp = "sudo rm -rf " + directory + path + "/web_static"
        run(temp)
        temp = "sudo rm -rf /data/web_static/current"
        run(temp)
        temp = "sudo ln -s " + directory + path + "/ /data/web_static/current"
        run(temp)
        return True
    except:
        return False
