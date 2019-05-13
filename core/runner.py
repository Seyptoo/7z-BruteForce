#!/usr/bin/env python
#coding:utf-8

import pzma
import options
import threading
import exceptions

class runner(threading.Thread):
    def __init__(self, output_condition=None, error_condition=None, output=threading=35):
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

        for i in range(int(self.output_threading)):
            wrapper = threading.Thread(target=self.eqs, args=(i, q))
            wrapper.setDaemon(True)
            wrapper.start()
            wrapper.join(600)

        q.join()
