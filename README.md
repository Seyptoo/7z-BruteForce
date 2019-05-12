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
    root@Computer:/home/Computer/Desktop# python server.py --files backup.7z --wordlist lists.txt
    [-] Password not found sorry : password
    [-] Password not found sorry : testing
    [-] Password not found sorry : gmail
    [-] Password not found sorry : backup
    [-] Password not found sorry : love
    [-] Password not found sorry : password123
    [-] Password not found sorry : bruteforce
    [-] Password not found sorry : server
    [-] Password not found sorry : love1234
    [-] Password not found sorry : attacker
    [-] Password not found sorry : proxy

    [+] Password 7z cracked with success : delete
