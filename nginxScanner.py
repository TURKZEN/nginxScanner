#! /usr/bin/python3

from ipaddress import ip_address as ipCheck
from validators import url as urlCheck
from sys import argv,exit

def usage():
    print("Usage : nginxScanner <IP>")
    exit()
try:
    IP = argv[1]
except:
    usage()
try:
    ipCheck(IP)

except ValueError:

    if not urlCheck(IP):
        usage()
    else:
        print("URL")
        
else:
    print("IP")


