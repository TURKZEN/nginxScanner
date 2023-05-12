#! /usr/bin/python3

from requests import get
from ipaddress import ip_address as ipCheck
from validators import url as urlCheck
from colorama import Fore
from sys import argv,exit

def usage():
    print(Fore.LIGHTGREEN_EX + """
Usage: nginxScanner <IP> or <URL>

EXAMPLES:

nginxScanner 192.168.1.1
nginxScanner https://www.example.com

    """)
    exit()

def detectionCVE(serverVersion):
    
    print(serverVersion)

def serverParser(serverType):
    
    serverType = str(serverType)
    try:
        serverType = serverType.split("/")
    except:
        print(Fore.RED + "Server type is not Nginx !")
        exit()
    else:
        try:
            serverName = serverType[0]
            serverVersion = serverType[1]
        except:
            print(Fore.RED + "Server type is not Nginx !")
            exit()
        else:
            if serverName == "nginx":
                detectionCVE(serverVersion)
            else:
                print(Fore.RED + "Server type is not Nginx !")
                exit()
def ip(IP):
    
    try:
        req = get("http://{}".format(IP))
    except:
        print(Fore.RED + "The server is unreachable !")
        print(Fore.RED + "The server may not be reachable by IP. \n If so try again with the URL.")
        exit()
    
    try:
        serverType = req.headers.get("Server")
    except:
        print(Fore.RED + "Server type cannot be determined")
        exit()
    else:
        serverParser(serverType)

def url(URL):
    
    try:
        req = get(URL)
    except:
        print(Fore.RED + "The server is unreachable !")
        exit()
    
    try:
        serverType = req.headers.get("Server")
    except:
        print(Fore.RED + "Server type cannot be determined")
        exit()
    else:
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
    banner = Fore.LIGHTGREEN_EX + """
━━━━━━━━━━━━━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━━━━━
┏━┓━┏━━┓┏┓┏━┓━┏┓┏┓┃┗━━┓┏━━┓┏━━┓━┏━┓━┏━┓━┏━━┓┏━┓
┃┏┓┓┃┏┓┃┣┫┃┏┓┓┗╋╋┛┗━━┓┃┃┏━┛┗━┓┃━┃┏┓┓┃┏┓┓┃┏┓┃┃┏┛
┃┃┃┃┃┗┛┃┃┃┃┃┃┃┏╋╋┓┃┗━┛┃┃┗━┓┃┗┛┗┓┃┃┃┃┃┃┃┃┃┃━┫┃┃━
┗┛┗┛┗━┓┃┗┛┗┛┗┛┗┛┗┛┗━━━┛┗━━┛┗━━━┛┗┛┗┛┗┛┗┛┗━━┛┗┛━
{}━━━━┏━┛┃━━━━━━━━━TURKZEN━OzlemBalci━━━━━━━━━━━━
━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{}github.com/TURKZEN/nginxScanner
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """.format(Fore.LIGHTMAGENTA_EX,Fore.LIGHTCYAN_EX )
    print(banner)

def Main():
    banner()
    verify()
    

if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print()
        print(Fore.LIGHTYELLOW_EX +"Logget out !")
    except EOFError:
        print()
        print(Fore.LIGHTYELLOW_EX +"Logget out")


