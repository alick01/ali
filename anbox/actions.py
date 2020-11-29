#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

#WorkDir="anbox-c898810050df67adccd64a84b2d763250a42e722"


def setup():
    shelltools.system("mkdir build")
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=/lib  \
            -DCMAKE_INSTALL_PREFIX=/usr  \
            -DBUILD_SHARED_LIBS=True  \
            -DWerror=OFF  \
            -DCMAKE_BUILD_TYPE=release")

def build():
    cmaketools.make()
        
        
def install():
    shelltools.cd("build")
    autotools.rawInstall("-C DESTDIR=%s" % get.installDIR())
    shelltools.system("rm '$pkgdir'/usr/bin/list_cpu_features")
    shelltools.system("rm '$pkgdir'/usr/lib/backward/BackwardConfig.cmake")
    shelltools.system("rm -r '$pkgdir'/usr/lib/cmake/CpuFeatures")
    shelltools.system("rm -r '$pkgdir'/usr/include")
    
    autotools.rawInstall("-m755 -D '$srcdir'/anbox-container-manager.initd '$pkgdir'/etc/init.d/anbox-container-manager")
    autotools.rawInstall("-m644 -D '$srcdir'/$pkgname.confd '$pkgdir'/etc/conf.d/$pkgname")
    autotools.rawInstall("-m755 -D '$srcdir'/$pkgname-launch.sh '$pkgdir'/usr/bin/$pkgname-launch")
    autotools.rawInstall("-m644 -D '$srcdir'/$pkgname.desktop '$pkgdir'/usr/share/applications/$pkgname.desktop")
    autotools.rawInstall("-m644 -D '$builddir'/snap/gui/icon.png '$pkgdir'/usr/share/icons/hicolor/512x512/anbox.png")
    
    autotools.rawInstall("-m755 -D '$builddir'/scripts/anbox-bridge.sh '$pkgdir'/usr/share/anbox/anbox-bridge.sh")
    autotools.rawInstall("-m755 -D '$builddir'/scripts/anbox-shell.sh '$pkgdir'/usr/share/anbox/anbox-shell.sh")
