#! /usr/bin/python3

from ipaddress import ip_address as ipCheck
from validators import url as urlCheck
from sys import argv,exit

def usage():
    print("""
    Usage: nginxScanner <IP> or <URL>
    
    EXAMPLES:

    nginxScanner 192.168.1.1
    nginxScanner https://www.example.com
    

    """)
    exit()

def ip():
    print("IP")

def url():
    print("URL")


def verify():
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
            url()
            
    else:
        ip()


def banner():
    pass


def Main():
    banner()
    verify()
    

if __name__ == "__main__":
    Main()



