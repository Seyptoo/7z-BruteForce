#coding:utf-8

import sys
import options

class DecryptErrorHash(Exception):
	def __init__(self, hash_spawn):
		# If decrypt is incorrect or hash.
		self.hash_spawn = hash_spawn
	
class InvalidErrorHash(Exception):
	def __init__(self, bert_hashs):
		# If hash is invalid got to error.
		self.bert_hashs = bert_hashs

class KalBinary(object):
	def __init__(self, hashs_decs=None):
		# Argument on called.
		self.encrypt = options.encrypt
		self.decrypt = options.decrypt
		self.validys = options.validys
		self.decs_hash = hashs_decs

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
		for propertys in range(0, 10000):
			for verboses in range(0,10000):
				wrapper = propertys + verboses
				# Loop for testing data. :D
				restricted = propertys - verboses
				restrictes = verboses - propertys
				multipdata = propertys * verboses
				
				modeexecs = int(propertys / verboses)
				modeexecd = int(verboses / propertys)

				if(modeexecs == int(octet_alogorithm)):
					self.decs_hash = ("%s/%s=") %(str(propertys), str(verboses))
				if(modeexecs == int(modeexecd)):
					self.decs_hash = ("%s/%s=") %(str(verboses), str(propertys))

				if(wrapper == int(octet_algorithm)):
					self.decs_hash = ("%s+%s=") %(str(propertys), str(verboses))
				if(restricted == int(octet_algorithm)):
					self.decs_hash = ("%s-%s=") %(str(propertys), str(verboses))
				if(restrictes == int(octet_algorithm)):
					self.decs_hash = ("%s-%s=") %(str(verboses), str(propertys))
				if(multipdata == int(octet_algorithm)):
					self.decs_hash = ("%s*%s=") %(str(propertys), str(verboses))

		return self.decs_hash


