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
import options
import platform
import exceptions

if(sys.version_info >= (2, 0) and sys.version_info <= (3, 0)):
    if(return_p.system("which 7z >/dev/null") != 0):
        raise exceptions.SevenZipNoInstall("Please install 7z in your computer.")

def seven_archive_exist(seven_archive):
    try:
        with open(seven_archive, "rb") as enumeration_file:
            enumeration_file = True
    except IOError as error_file_output:
        enumeration_file = False

    # The return value in function __seven_archive_exist()__,
    # is exactly here my friends for calling after function().

    return enumeration_file

def decompress_data(filename_archive, end_password):
    '''
       This function is used to decrypt
       the file __decompress_data()__.
    '''
    property_c = " "

    if(seven_archive_exist(options.files) == True):
        method_req  = __name__["DECOMPRESS"] + property_c
        method_req += __name__["COMPRESS"] + property_c
        method_req += __name__["DECOMPRESS_PASSWORD"] + end_password + property_c
        method_req += options.files + property_c
        method_req += __name__["COMPRESS_PASSWORD"] + property_c
        method_req += __name__["BINARY_STRINGS"]

    if(return_p.system(method_req) == 0):
        method_req = True
    else:
        method_req = False

    return method_req
