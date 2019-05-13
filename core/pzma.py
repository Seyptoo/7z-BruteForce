#/usr/bin/env python
#coding:utf-8

__all__ = ["DECOMPRESS", "COMPRESS", "DECOMPRESS_PASSWORD", "COMPRESS_PASSWORD",
            "BINARY_STRINGS", "SPEED_BRUTEFORCE", "NEGATIVE_OUTPUT", "DIRECT_NULL"]

__name__ = {
    __all__[0]:"7z",
    __all__[1]:"x",
    __all__[2]:"-p",
    __all__[3]:"-aoa",
    __all__[4]:">/dev/null"
    }

'''
This module will do a lot of things to
manage the attacks and do a lot of manipulation.
'''

import os as return_p
import re
import sys
import shutil
import platform

from core import exceptions
from core import options

if(sys.version_info >= (2, 0) and sys.version_info <= (3, 0)):
    if(return_p.system("which 7z >/dev/null") != 0):
        raise exceptions.SevenZipNoInstall("Please install 7z in your computer.")

class pzma_br(object):
    def __init__(self, enumeration_file=None, property_c=" "):
        self.enumeration_file = enumeration_file
        self.property_c       = property_c

    def seven_archive_exist(seven_archive):
        '''
            Lets you test if the 7z file exists in the computer system
            in function for check __check_filenames__().
        '''
        try:
            with open(seven_archive, "rb") as self.enumeration_file:
                self.enumeration_file = True
        except IOError as error_file_output:
            self.enumeration_file = False

        # The return value in function __seven_archive_exist()__,
        # is exactly here my friends for calling after function().

        return self.enumeration_file

    def decompress_data(filename_archive, end_password):
        '''
        This function is used to decrypt
        the file __decompress_data()__.
        '''
        method_req  = __name__["DECOMPRESS"] + self.property_c
        method_req += __name__["COMPRESS"] + self.property_c
        method_req += __name__["DECOMPRESS_PASSWORD"] + end_password + self.property_c + options.files + self.property_c
        method_req += __name__["COMPRESS_PASSWORD"] + self.property_c
        method_req += __name__["BINARY_STRINGS"]

        if(return_p.system(method_req) == 0):
            password_bool = True
        elif(return_p.system(method_req) != 0):
            password_bool = False

        # So concretely it will return true or
        # false if the password is wrong or not decompress_data()

        return password_bool
