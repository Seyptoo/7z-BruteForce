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

from core import options
from core import exceptions

class pzma_br(object):
    def __init__(self, section_one=None, section_two=None, section_four=" ",
                section_five=None, section_six=None):
	'''
            I have created some options for the object for the care of the
            program __pzma_br()__.            		
	'''
        self.section_one   = section_one
	self.section_two   = section_two
        self.section_four  = section_four
        self.section_five  = section_five
        self.section_six   = section_six

    def seven_which_exist(self):
        '''
            This function will test if the
            7z program exists in the computer system __seven_which_exist()__.
        '''
        if(sys.version_info >= (2, 0) and sys.version_info <= (3, 0)):
                if(return_p.system("which 7z >/dev/null") != 0):
                    self.section_six = False

                elif(return_p.system("which 7z >/dev/null") == 0):
                    self.section_six = True

        # the return value in function __seven_which_exist__().
        # if 7z in the path return true or return false.

        return self.section_six

    def seven_archive_exist(self, seven_archive):
        '''
            Lets you test if the 7z file exists in the computer system
            in function for check __check_filenames__().
        '''
        try:
            with open(seven_archive, "rb") as self.section_one:
                self.section_one = True
        except IOError as error_file_output:
            self.section_one = False

        # The return value in function __seven_archive_exist()__,
        # is exactly here my friends for calling after function().

        return self.section_one

    def seven_decompress_data(self, seven_filename, seven_password):
        '''
            This function is used to decrypt
            the file __decompress_data()__.
        '''
        section_three = " "
        section_two   = __name__["DECOMPRESS"] + section_three
        section_two  += __name__["COMPRESS"] + section_three
        section_two  += __name__["DECOMPRESS_PASSWORD"] + seven_password + section_three + options.files + section_three
        section_two  += __name__["COMPRESS_PASSWORD"] + section_three
        section_two  += __name__["BINARY_STRINGS"]

        if(return_p.system(section_two) == 0):
            self.section_four = True

        elif(return_p.system(section_two) != 0):
            self.section_four = False

        # So concretely it will return true or
        # false if the password is wrong or not decompress_data()

        return self.section_four

    def seven_check_file(self, seven_check):
        '''
            This function is used to test if
            the file is a 7zip file __pzma_file()__.
        '''
        if(seven_check.endswith(".7z") == False):
            self.section_five = False

        elif(seven_check.endswith(".7z") == True):
            self.section_five = True

        # So this function allows to test if the program is a 7z file.
        # the function name is pzma_br().pzma_file().

        return self.section_five

if __name__ == "__main__":
    pass
