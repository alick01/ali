#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("truncate -s 0 tests/CMakeLists.txt")
    shelltools.system("mkdir build")
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=/usr/lib  \
        -DCMAKE_INSTALL_PREFIX=/usr  \
        -DCMAKE_BUILD_TYPE=Release  \
        -DCMAKE_LD_FLAGS=NO  \
        -Wno-dev")

def build():
    
    autotools.make()
    

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
