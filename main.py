#!/usr/bin/env python 
#coding:utf-8

import sys
import platform
import threading
import subprocess
import os as return_p

from core import options
from core import exceptions

class SevenZip(threading.Thread):
	def __init__(self, threads=100, command=0):
		threading.Thread.__init__(self)
		'''
			create function for call after
			the variable __init__().
		'''
		self.threads_tds = threads
		self.command_tds = command
		self.argument_on = options.files
		self.argument_wd = options.wordlist

		if(self.argument_on == None and self.argument_wd == None):
			sys.exit(return_p.system("python %s -h" %(sys.argv[0])))
		elif(self.argument_on == None or self.argument_wd == None):
			sys.exit(return_p.system("python %s -h" %(sys.argv[0])))

	def is_tool(self):
		'''
			This function is used to test whether
			the 7z program exists on the computer __is_tool(self)__.
		'''
		if(platform.system() == "Linux"):
			if(return_p.system("which 7z >/dev/null") != 0):
				raise exceptions.SevenZipNoInstall("Please install 7z in your computer.")
				
		elif(platform.system() == "Windows"):
			if(return_p.system("where /7z > NUL") != 0):
				raise exceptions.SevenZipNoInstall("Please install 7z in your computer.")

	def ExtensionModel(self, q):
		"""
		This function will attack
		the file 7z is to hack the file

		Parameters
		----
			self : They are supervariables or they can communicate anywhere
			q : The variable q is the wordlist is called

		Returns
		----
			This function will return 
			the attack and password cracker
		"""
		print("Copyright (c) 2019 by Seyptoo.")
		if(self.argument_on.endswith(".7z") == True):
			ptr_count = 0
			while True:
				command_list = q.get()
				command_send = "7z x -p%s %s -aoa >/dev/null" %(command_list, self.argument_on)
				self.command = return_p.system(command_send)

				if(self.command == 0):
					print("\n[SUCCESS] Password cracked with success : %s\n" %(command_list))
					sys.exit(0)

				elif(self.command != 0): 
					count_line = len(open(self.argument_wd).readlines())
					ptr_count = ptr_count + 1
					reads_line = "\r7z-Bruteforce cracker password, version 1.0.0.0-7z-1 %d/%d." %(ptr_count, count_line)
					sys.stdout.write(reads_line)
					sys.stdout.flush()
					
		else:
			raise exceptions.SevenZipIncorrect("File is extensions incorrect.")

	def run(self):
		"""
		This function will optimize the 
		program by boosting it with threads

		Parameters
		----
			self : They are supervariables or they can communicate anywhere
	
		Returns
		----
			This function will not return much
		"""
		if(sys.version_info >= (2, 0)):
			import queue
			q = queue.Queue()
		else:
			import Queue
			q = Queue.Queue()

		# So concretely the system of threads that passes here in this function.
		# The default thread is 100 to handle the GPU __run__().

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
	Algorithm.is_tool()
	Algorithm.start()
