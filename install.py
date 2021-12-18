import os
import sys
import time
import urllib2
import json
import base64
from termcolor import colored, cprint
from base64 import *
red = "\33[31;1m"
green = "\33[32;1m"
yellow = "\33[33;1m"
white = "\33[37;1m"
def main_write(a):
        for b in a + '\n':
                sys.stdout.write(b)
                sys.stdout.flush()
                time.sleep(1./100)
def main_script():
        time.sleep(1)
        os.system("clear")
        os.system("pkg install python -y")
        os.system("pkg install python2 -y")
        os.system("pkg install nano -y")
        os.system("pkg install curl -y")
        main_file_requirements = open("requirements.txt", "w")
        code_requirements = 'termcolor\ncolored\ncprint'
        main_file_requirements.write(code_requirements)
        main_file_requirements.close()
        main_write(green+"TOOLS HACKER CREATED BY ITZHEX - VERSION 1.9.8 - HAVE FUN IN CYBERSPACE")
main_script()
        