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
        print("")
        question1()
def question1():
        question1 = raw_input("Are You Sure You Want To Continue? {Y/n]: ")
        if question1 == "Y" or question1 == "y":
                time.sleep(1)
                print("")
                main_write("installing start.py ...")
                main_installing()
                main_write("Installing start.py Done ...")
                print("")
                main_write("Copying Files data ...")
                main_copying()
                main_write("Copying Files data Done ...")
                print("")
                main_write("Copying Files log ...")
                main_copying()
                main_write("Copying Files log Done ...")
def main_installing():
        print("")
        print("TOOLS HACKING | INSTALLING")
        print("--------------------------")
        main_write("[*] 10%")
        main_write("[**] 20%")
        main_write("[***] 30%")
        main_write("[****] 40%")
        main_write("[*****] 50%")
        main_write("[******] 60%")
        main_write("[*******] 70%")
        main_write("[********] 80%")
        main_write("[*********] 90%")
        main_write("[**********] 100%")
        print("--------------------------")
def main_copying():
        print("")
        print("TOOLS HACKING | COPYING")
        print("--------------------------")
        main_write("[*] 10%")
        main_write("[**] 20%")
        main_write("[***] 30%")
        main_write("[****] 40%")
        main_write("[*****] 50%")
        main_write("[******] 60%")
        main_write("[*******] 70%")
        main_write("[********] 80%")
        main_write("[*********] 90%")
        main_write("[**********] 100%")
        print("--------------------------")
main_script()