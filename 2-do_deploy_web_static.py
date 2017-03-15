#!/usr/bin/python3
# distributes an archive to our web servers
from fabric.api import *
env.hosts = ['52.90.159.84', '54.242.30.104']


def do_deploy(archive_path):
    """ upload archive and delete from web server"""
    try:
        put(archive_path, "/tmp/")
        path = archive_path.strip("versions/")
        directory = "/data/web_static/releases/"
        temp = "sudo mkdir -p " + directory + path
        run(temp)
        temp = "sudo tar -xzf /tmp/" + path + " -C " + directory + path
        run(temp)
        run("rm /tmp/" + path)
        temp = "sudo mv " + directory
        temp += "/web_static/* " + directory + path + "/"
        run(temp)
        temp = "sudo rm -rf " + directory + path + "/web_static"
        run(temp)
        temp = "rm -rf " + directory
        run(temp)
        temp = "sudo ln -s " + directory + path + "/ /data/web_static/current"
        run(temp)
        return True
    except:
        return False
