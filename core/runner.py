#!/usr/bin/env python
#coding:utf-8

import pzma
import options
import exceptions

class runner(object):
    def __init__(self, output_condition=None, error_condition=None):
        self.output_condition = pzma.pzma_br()
        self.error_condition  = error_condition

    def __str__(self):
        if(self.output_condition.seven_which_exist() == False):
            raise SevenZipNoInstall("7z is not installed in your computer.")

        if(self.output_condition.seven_archive_exist(options.files) == False):
            raise SevenZipNoFound("7z files is not found in your computer.")

        if(self.output_condition.seven_check_file(options.files) == False):
            raise SevenZipIncorrect("7z, please select archive file .7z.")
