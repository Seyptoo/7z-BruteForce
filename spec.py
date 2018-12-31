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
				CalculationBytes=None,
				CalculationOctet=None,
				ArgumentationFal=None,
				AlphabetEu=None):

		self.CalculationBytes = CalculationBytes
		self.CalculationOctet = CalculationOctet
		self.ArgumentationFal = ArgumentationFal
		self.AlphabetEu = AlphabetEu
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
					self.ArgumentationFal = "%s/%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))
				if SecondValue == int(octet_algorithm):
					self.ArgumentationFal = "%s/%s=" % (str(self.CalculationOctet), str(self.CalculationBytes))
				
				# We are in a condition that will test specific variables like the variable #FirstValue #SecondValue
				# Variables that behave in a way with bytes.

				if AddModel == int(octet_algorithm):
					self.ArgumentationFal = "%s+%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))
				if SubModel == int(octet_algorithm):
					self.ArgumentationFal = "%s-%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))

				# We do not have supervariables like for example with the selfs or that kind of thing.
				# But it's always good to have the selfs to communicate the variables everywhere.

				if Sub_Model == int(octet_algorithm):
					self.ArgumentationFal = "%s-%s=" % (str(self.CalculationOctet), str(self.CalculationBytes))
				if MulModel == int(octet_algorithm):
					self.ArgumentationFal = "%s*%s=" % (str(self.CalculationBytes), str(self.CalculationOctet))

		return self.ArgumentationFal
	
	def BertPanel(self, BinaryArg):
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
		self.AlphabetEu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.AlphabetEu = list(self.AlphabetEu)
	
		ArgumentCrypt = ""
	
		for Carling in BinaryArg:
			try:
				# Create loop for hashing.
				Carling = int(Carling)
				NewUses = self.AlphabetEu[car]
				ArgumentCrypt += NewUses
				# Create loop for hashing.
			except:
				ArgumentCrypt += Carling
			
		return(ArgumentCrypt)
	
	def BertBinary(self, ArgumentTexte):
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
		ArgumentOctets = [ bin(ord(ch))[2:].zfill(8) for ch in ArgumentTexte ]
		ArgumentList = []
	
		for BytesArgument in ArgumentOctets:
			SegmentOne = BytesArgument[:3]
			SegmentTwo = BytesArgument[3:]
		
			ArgumentList.append(SegmentOne)
			ArgumentList.append(SegmentTwo)
		
		return(ArgumentList)

	def run(self): 

		calc_text = ""

		bin_list = self.BertBinary(ArgumentTexte)

		for octet in bin_list:
			calcul = self.BertModel(octet_algorithm)
			calc_text += calcul

		final_crypt = self.BertPanel(calc_text)
		print("HASH : "+final_crypt)

if __name__ == "__main__":
	Algorithm = KalBinary()
	Algorithm.run()	
