#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "JELVIS-git-master"


def install():
    pisitools.insinto("/usr/bin", "./jelvis-assistant")
    pisitools.insinto("/usr/share/icons", "./icons/jelvis.png")
    pisitools.insinto("/usr/share/icons", "./icons/jelvis_try.png")
    pisitools.insinto("/usr/share/applications", "./jelvis.desktop")
    pisitools.insinto("/opt/jelvis", "./*")
    shelltools.system("chmod 00755 %s/opt/jelvis/*" % get.installDIR())
    shelltools.system("chmod 00755 %s/opt/jelvis/icons/*" % get.installDIR())
