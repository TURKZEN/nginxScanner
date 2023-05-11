#! /usr/bin/python3

from requests import get
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
    
def serverParser(serverType):
    print(serverType)

def ip(IP):
    print("IP")
    req = get("http://{}".format())
    serverType = req.headers.get("Server")
    serverParser(serverType)

def url(URL):
    print("URL")
    req = get(URL)
    serverType = req.headers.get("Server")
    serverParser(serverType)

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
            URL = IP
            url(URL)
            
    else:
        ip(IP)


def banner():
    pass


def Main():
    banner()
    verify()
    

if __name__ == "__main__":
    Main()



