#coding:utf-8

import sys
import os as subprocessing
import Queue
import threading
import optparse

class SevenZipIncorrect(Exception):
	def __init__(self, error_zip):
		self.error_zip = error_zip

class SevenZip(threading.Thread):
	def __init__(self, threads=35, command=None):
		threading.Thread.__init__(self)
		# System of Threads is present
		self.threads_tds = threads
		self.command_tds = command

		self.argument_on = sys.argv[1]
		self.argument_wd = sys.argv[2]

	def ExtensionModel(self, q):
		"""
		This function will attack
		the file 7z is to hack the file

		Parameters
		----
			self : They are supervariables or they can communicate anywhere
			q = The variable q is the wordlist is called

		Returns
		----
			This function will return 
			the attack and password cracker
		"""
		if(self.argument_on.endswith(".7z") == True):
			while True:
				BertModel = q
				BertModel = BertModel.get()
				# Execution command for bruteforce ! :D
				self.command_tds = ("7z x -p%s %s -aoa >/dev/null" %(BertModel, self.argument_on))
				output_status_ts = subprocessing.system(self.command_tds)
				# Starting bruteforce ! :D
				if(output_status_ts == 0):
					print "\n[+] Password cracked with success : %s\n" %(BertModel)
					sys.exit(1)
				else: # If password is not cracked.
					print "[-] Password not cracked : %s" %(BertModel)

		else: # exceptions error
			raise SevenZipIncorrect("File is extensions incorrect")

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
