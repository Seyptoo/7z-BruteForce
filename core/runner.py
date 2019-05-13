#!/usr/bin/env python
#coding:utf-8

import sys
import pzma
import threading

from core import options
from core import exceptions

class runner(threading.Thread):
    def __init__(self, error_condition=None, output_threading=100, nb_check=0):
        threading.Thread.__init__(self)
        '''
            create function for call after
            the variable __init__().
        '''
        self.error_condition  = error_condition
        self.output_threading = output_threading
        self.nb_check         = nb_check

    def __str__(self):
        '''
            This function is used to
            manage program errors __str__()
        '''
        if(pzma.pzma_br().seven_which_exist() == False):
            raise exceptions.SevenZipNoInstall("7z is not installed in your computer.")

        if(pzma.pzma_br().seven_archive_exist(options.files) == False):
            raise exceptions.SevenZipNoFound("7z files is not found in your computer.")

        if(pzma.pzma_br().seven_check_file(options.files) == False):
            raise exceptions.SevenZipIncorrect("7z, please select archive file .7z.")

    def eqs(self, q):
        '''
            Concretely this function will
            manage the attack of the archive __eqs__().
        '''
        while True:
            qs = q.get()
            if(pzma.pzma_br().seven_decompress_data(options.files, qs) == True):
                print("\n[SUCESS] Password archive cracked : %s" %(qs))
                sys.exit(0)

            else:
                self.nb_check = self.nb_check + 1
                read_file_count = len(open(options.wordlist, "r").readlines())
                read_line_count = "\r7z-Bruteforce cracker password, version 1.0.0.0-7z-1 %d/%d." %(self.nb_check, read_file_count)

                # This condition will allow attacking the archive.
                # in function __eqs__().

                sys.stdout.write(read_line_count)
                sys.stdout.flush()

    def run(self):
        '''
            This system makes it possible to
            accelerate bruteforce __run__()
        '''
        if(sys.version_info >= (2, 0)):
            import queue
            q = queue.Queue()

        elif(sys.version_info <= (3, 0)):
            import Queue
            q = Queue.Queue()

        # So concretely the system of threads that passes here in this function.
        # The default thread is 100 to handle the GPU __run__().

        with open(options.wordlist, "r") as bert_model:
            for queue_reverse in bert_model:
                q.put(queue_reverse.rstrip("\n\r"))
            self.eqs(q)

        for i in range(int(self.output_threading)):
            wrapper = threading.Thread(target=self.eqs(), args=(i, q))
            wrapper.setDaemon(True)
            wrapper.start()
            wrapper.join(600)

        q.join()
