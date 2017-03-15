#!/usr/bin/python3
# makes a tarball by using fabric local to call shell commands
from fabric.api import *


def do_pack():
    """ tarballs web_static"""
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -zcvf \"./versions/web_st\
        atic_`date +%Y%m%d%H%M%S`.tgz\"web_static")
    except:
        return None
