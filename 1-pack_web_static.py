#!/usr/bin/env python3
"""
Fabric script for create a zip file for all
web static
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Function that generate a .tgz 
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "version/web_static{}.tgz".format(time)
    try:
        local("mkdir -p ./version")
        local("tar -zcvf {} ./web_static".format(file_name))
        return file_name
    except:
        return None
