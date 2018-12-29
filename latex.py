#coding:utf-8

import sys
import os
import Queue
import threading
import optparse
import py7zlib

class SevenZipIncorrect(Exception):
	def __init__(self, error_zip):
		self.error_zip = error_zip

class SevenZip(threading.Thread):
	def __init__(self, threads=35):
		threading.Thread.__init__(self)
		# System of Threads is present
		self.threads_tds = threads
		self.argument_on = sys.argv[1]
		self.argument_wd = sys.argv[2]

	def ExtensionModel(self, q):
		if(self.argument_on.endswith(".7z") == True):
			while True:
				BertModel = q
				BertModel = BertModel.get()
		else: # exceptions error
			raise SevenZipIncorrect("ExtensionFileIncorrect")

	def run(self):
		q = Queue.Queue()
		with open(self.argument_wd, "r") as BertModel:
			for Queue_Reverse in BertModel:
				q.put(Queue_Reverse.rstrip("\n\r"))
			self.ExtensionModel(q)

		for i in range(int(self.threads_tds)):
			wrapper = threading.Thread(target=self.ExtensionModel, args=(i, q))
			wrapper.setDaemon(True)
			wrapper.start()
			wrapper.join(600)

		q.join()

if __name__ == "__main__":
	Algorithm = SevenZip()
	Algorithm.start()
