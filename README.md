# 7z-BruteForce

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Options
----
There are two options available in the program, --files and --wordlist.

    Usage: latex.py [options]

    Options:
      -h, --help            show this help message and exit
      -f FILES, --files=FILES
                            The 7z file to crack.
      -w WORDLIST, --wordlist=WORDLIST
                            The wordlist for crack.

Development
----

This program was developed under linux, because the file 7z is already installed by default on Linux but the program can work very well under Windows if you manage a little alone.

    Linux

Use :
----

As you can see, you have to use 2 functions to run the program. The --files option for the 7z file name and finally --wordlist for the file list that will test the passwords.

    root@Computer:/home/Computer/Desktop# python server.py --files backup.7z --wordlist lists.txt
    Copyright (c) 2019 by Seyptoo.
    7z-Bruteforce cracker password, version 1.0.0.0-7z-1 467/220563.
    [SUCCESS] Password cracked with success : password
