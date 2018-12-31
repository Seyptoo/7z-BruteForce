#coding:utf-8

import sys
import subprocess
import os
import options as argument

CHECK_VERSION = sys.version_info <= (3,0)
if(CHECK_VERSION):
	sys.exit("[-] Version of Python is incorrect")

class KalBinary(object):
	def __init__(self,
				algorithms_params=None,
				CalculationBytes=None,
				CalculationOctet=None,
				hash_dec=None):

		self.algorithms = algorithms_params
		self.CalculationBytes = CalculationBytes
		self.CalculationOctet = CalculationOctet
		self.hash_dec = hash_dec
		self.encrypt = argument.encrypt

	def BertModel(self, octet_algorithm):
		"""
		This function will handle
		the data encryption.

		Parameters
		----
		self : They are supervariables or they can communicate anywhere
		octet_algorithm : The bytes of the variable

		Returns
		----
		Returns octets with success and brow.
		finished.
		"""
		for self.CalculationBytes in range(0, 10000):
			for self.CalculationOctet in range(0, 10000):
				# Create loop for hashing.
				AddModel = self.CalculationBytes + self.CalculationOctet
				SubModel = self.CalculationBytes - self.CalculationOctet
				Sub_Model = self.CalculationOctet - self.CalculationBytes
				MulModel  = self.CalculationBytes * self.CalculationOctet

				FirstValue = int(self.CalculationBytes / self.CalculationOctet)
				SecondValue = int(self.CalculationOctet / self.CalculationBytes)

				if FirstValue == int(octet_algorithm):
					self.hash_dec = "%s/%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))
				if SecondValue == int(octet_algorithm):
					self.hash_dec = "%s/%s=" % (str(self.CalculationOctet), str(self.CalculationBytes))
				
				# We are in a condition that will test specific variables like the variable #FirstValue #SecondValue
				# Variables that behave in a way with bytes.

				if AddModel == int(octet_algorithm):
					self.hash_dec = "%s+%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))
				if SubModel == int(octet_algorithm):
					self.hash_dec = "%s-%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))

				# We do not have supervariables like for example with the selfs or that kind of thing.
				# But it's always good to have the selfs to communicate the variables everywhere.

				if Sub_Model == int(octet_algorithm):
					self.hash_dec = "%s-%s=" % (str(self.CalculationOctet), str(self.CalculationBytes))
				if MulModel == int(octet_algorithm):
					self.hash_dec = "%s*%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))

		return self.hash_dec
