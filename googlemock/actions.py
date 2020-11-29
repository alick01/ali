#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools




def setup():
    shelltools.system("mkdir build")
    shelltools.cd("build")
    shelltools.system("cmake ..")
    
def build():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DBUILD_SHARED_LIBS=ON \
        -DPYTHON_EXECUTABLE=python3 \
        -DBUILD_GMOCK=ON \
        -DINSTALL_GTEST=ON \
        -Dgtest_build_tests=ON")
    
def install():
    autotools.rawInstall()
    #pisitools.dolib("build/*.so")
    pisitools.dobin("googlemock/scripts/gmock-config.in")
    shelltools.chmod("googlemock/include", 0755)
    pisitools.insinto("/usr/lib/pkgconfig/googletest/googlemock/*.pc", "googlemock/cmake/*.pc.in")
    pisitools.insinto("/usr/src/googletest/googlemock/include/gmock", "googlemock/include/gmock/*.h")
    pisitools.insinto("/usr/src/googletest/googlemock/include/gmock/internal", "googlemock/include/gmock/internal/*.h")
    pisitools.insinto("/usr/src/googletest/googlemock/src", "googlemock/src/*")
    pisitools.insinto("/usr/src/googletest/googlemock/scrpits", "googlemock/scripts/*")
    pisitools.insinto("/usr/src/googletest/googlemock/test", "googlemock/test/*")
    pisitools.insinto("/usr/src/googletest/googlemock/docs", "googlemock/docs/*")
    pisitools.insinto("/usr/src/googletest/googlemock", "CMakeLists.txt")
    pisitools.insinto("/usr/src/googletest/googlemock/cmake", "googlemock/cmake/*")
    pisitools.dodoc("WORKSPACE", "CONTRIBUTING.md", "LICENSE", "README.md")
