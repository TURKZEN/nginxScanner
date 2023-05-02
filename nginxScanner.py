#! /usr/bin/python3

import requests
from sys import argv,exit

def serverDetection():
    try:
        ip = argv[1]
    except:
        return "Usage: nginxScanner <IP>"
        exit()
    else:
        try:
            req = requests.get("http://{}".format(ip))
            return req.headers.get("server")
        except:
            print("""
            Error !

            Could not detect server type.
            """)
            exit()
def banner():
    pass

def Main():
    banner()
    serverType = serverDetection()
    print(serverType)



if __name__ == "__main__":
    Main()