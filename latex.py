#coding:utf-8
# Coded by Seyptoo

import sys
import os as command_execution

class SevenZipIncorrect(Exception):
	def __init__(self, error_7zip):
		self.error_7zip = error_7zip

class SevenZip(object):
	def __init__(self):
		# Create argument with sys ! :D
		self.files_7z = sys.argv[1]
		self.wordlist = sys.argv[2]

	def SevenZIP(self):
		if(self.files_7z.endswith(".7z") == True):
			with open(self.wordlist, "r") as file:
				file = file.readlines()
				# Read files ! :)
			for file_output in file:
				# Create loop for bruteforce ! :D
				file_output = file_output.strip("\n")
				send_cmd = "7z x -p%s %s -aoa >/dev/null" %(file_output, self.files_7z)
				# Creating command for sending ! :D
				BertModel = command_execution.system(send_cmd)

				if not(BertModel == 0):
					print "[-] Password not found sorry : %s" %(file_output)
				else:
					print "\n[+] Password 7z cracked with success : %s\n" %(file_output)
					sys.exit(0)

		elif not(self.files_7z.endswith(".7z")):
			raise SevenZipIncorrect("Error file extension")

if __name__ == "__main__":
	Algorithm = SevenZip()
	Algorithm.SevenZIP()
