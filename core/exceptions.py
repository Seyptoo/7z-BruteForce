#/usr/bin/env python
#coding:utf-8

class SevenZipIncorrect(Exception):
	def __init__(self, error_zip):
		self.error_zip = error_zip

class SevenZipNoInstall(Exception):
	def __init__(self, error_dls):
		self.error_dls = error_dls
