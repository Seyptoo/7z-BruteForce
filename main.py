#!/usr/bin/env python
#coding:utf-8

import sys
import os as return_n

from core import exceptions
from core import options
from core import runner
from core import pzma

class call(object):
    def __init__(self):
        if(options.files == None or options.wordlist == None):
            sys.exit(return_n.system("python %s -h" %(sys.argv[0])))
        sys.exit(runner.runner().start()) 

if __name__ == "__main__":
    call().__init__()
