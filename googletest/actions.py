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
    pisitools.dobin("googletest/scripts/gtest-config.in")
    shelltools.chmod("/usr/include", 0755)
    pisitools.insinto("/usr/src/googletest/googletest/include/gtest", "googletest/include/gtest/*.h")
    pisitools.insinto("/usr/src/googletest/googletest/include/gtest/internal", "googletest/include/gtest/internal/*.h")
    pisitools.insinto("/usr/share/gtest", "CMakeLists.txt")
    pisitools.insinto("/usr/lib/pkgconfig/googletest/*.pc", "googletest/cmake/*.pc.in")
    pisitools.insinto("/usr/src/googletest/googletest/cmake", "googletest/cmake/*")
    pisitools.insinto("/usr/src/googletest/googletest/docs", "googletest/docs/*")
    pisitools.insinto("/usr/src/googletest/googletest/samples", "googletest/samples/*")
    pisitools.insinto("/usr/src/googletest/googletest/scripts", "googletest/scripts/*")
    pisitools.insinto("/usr/src/googletest/googletest/src", "googletest/src/*")
    pisitools.insinto("/usr/src/googletest/googletest/test", "googletest/test/*")
    pisitools.dodoc("WORKSPACE", "CONTRIBUTING.md", "LICENSE", "README.md")
