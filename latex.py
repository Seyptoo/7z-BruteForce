#coding:utf-8

import sys
import requests
import options as argument
import Queue

from optparse import *
from threading import Thread

class pyDirb(Thread):
	def __init__(self, threads=35):
		# options create on 'options.py'.
		self.URL = argument.url
		self.WORDLIST = argument.wordlist
		self.DIRECTORY = argument.directory

		self.THREADS = threads
		Thread.__init__(self)

	def brute_functions(self, q):
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
		if(self.DIRECTORY == True):
			while True:
				wordlist_boolen = q.get()

	def run(self):
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
		q = Queue.Queue()

		with open(self.WORDLIST, "r") as file:
			for line_strip in file:
				q.put(line_strip.rstrip("\n\r"))

			self.brute_functions(q)

		for i in self.THREADS:
			wrapper = threading.Thread(target=self.brute_functions(i), args=(i, q))
			wrapper.setDaemon(True)
			wrapper.start()
			wrapper.join(600)

		q.join()

if __name__ == "__main__":
	Algorithm = pyDirb()
	Algorithm.start()
