#!/usr/bin/env python
#coding:utf-8

import pzma
import options
import threading
import exceptions

class runner(threading.Thread):
    def __init__(self, output_condition=None, error_condition=None, output_threading=35):
        threading.Thread.__init__(self)
        '''
            create function for call after
            the variable __init__().
        '''
        self.output_condition = pzma.pzma_br()
        self.error_condition  = error_condition
        self.output_threading = output_threading

    def __str__(self):
        '''
            This function is used to
            manage program errors __str__()
        '''
        if(self.output_condition.seven_which_exist() == False):
            raise exceptions.SevenZipNoInstall("7z is not installed in your computer.")

        if(self.output_condition.seven_archive_exist(options.files) == False):
            raise exceptions.SevenZipNoFound("7z files is not found in your computer.")

        if(self.output_condition.seven_check_file(options.files) == False):
            raise exceptions.SevenZipIncorrect("7z, please select archive file .7z.")

if __name__ == "__main__":
    runner()
