#!/usr/bin/env python 
#coding:utf-8

from optparse import *

parser = OptionParser()
parser.add_option("-f", "--files", dest="files", help="The 7z file to crack.")
parser.add_option("-w", "--wordlist", dest="wordlist", help="The wordlist for crack.")
(options, args) = parser.parse_args()
files = options.files
wordlist = options.wordlist
