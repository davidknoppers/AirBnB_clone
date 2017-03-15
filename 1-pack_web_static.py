#!/usr/bin/python3
# makes a tarball by using fabric local to call shell commands
from fabric.api import local
import time

def do_pack():
    """ tarballs web_static"""
    filename = "web_static_{:s}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    try:
        local("sudo mkdir -p versions")
        local("tar -cvzf versions/{} web_static/".format(filename))
    except:
        return None
