#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import platform
import os as return_p

__version__     = "1.0.0.0"
__authors__     = "Seyptoo"
__description__ = "Crack archive 7zip"
__name__        = "7z-BruteForce"

'''
    This function allows you to install
    the necessary packages and run the program __setup__tools()__.
'''

if(platform.dist()[0] == "Ubuntu" or platform.dist()[0] == "Debian"):
    bash_command = """
    apt-get install p7zip-full
    """
else: 
    bash_command = """
    pacman -S p7zip
    """

return_p.system(bash_command)
setuptools.setup (
    name = __name__,
    author = __authors__,
    version = __version__,
    description = __description__
)

if __name__ == "__main__":
  pass
