#/usr/bin/env python
#coding:utf-8

__all__ = ["DECOMPRESS", "COMPRESS", "DECOMPRESS_PASSWORD", "COMPRESS_PASSWORD",
            "BINARY_STRINGS", "SPEED_BRUTEFORCE", "NEGATIVE_OUTPUT"]

__name__ = {
    "-p"  :__all__[0],
    "-x"  :__all__[2],
    "-aoa":__all__[::-1]
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
    '''
        Lets you test if the 7z file exists in the computer system
        __check_filenames__().
    '''
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
    if(seven_archive_exist(options.files) == True):
        pass
