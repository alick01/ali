#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
import os
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    # libpng15 fix    
    shelltools.system("setconf src/tuxpaint.desktop Categories='Game;KidsGame;Graphics;RasterGraphics;'")
    shelltools.system("setconf -u src/tuxpaint.conf fullscreen=true")
    shelltools.system("setconf Makefile COMPLETIONDIR='s/usr/share/bash-completion/completions'")
    shelltools.system("setconf Makefile ARCH_INSTALL=''")
    
    
    autotools.make()

def install():
   autotools.install("DESTDIR=%s" % get.installDIR())
   docdir = "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME())
   autotools.rawInstall("PKG_ROOT=%s DOC_PREFIX=%s" % (get.installDIR(), docdir))
   
for size in ("16", "22", "32", "48", "64", "96", "128", "192"):
    pisitools.insinto("data/images/tuxpaint.png", "/usr/share/icons/hicolor/%sx%s/apps" % (size, size),
                           "tux4kids-tuxpaint.png")

