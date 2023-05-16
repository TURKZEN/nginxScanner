#! /usr/bin/python3

import requests
from ipaddress import ip_address as ipCheck
from validators import url as urlCheck
from colorama import Fore
from CVEs import CVEs
from sys import argv,exit
from os import name as osName

def usage():
    print(Fore.LIGHTGREEN_EX + """
Usage: nginxScanner <IP> or <URL>

EXAMPLES:

nginxScanner 192.168.1.1
nginxScanner https://example.com

    """)
    exit()

def winUsage():
    print(Fore.LIGHTGREEN_EX + """
Usage: python nginxScanner <IP> or <URL>

EXAMPLES:

python nginxScanner 192.168.1.1
python nginxScanner https://example.com

    """)
    exit()

def serverPrint(serverVersion):
    print(Fore.RESET + "Server : ",Fore.RED,argv[1])
    print(Fore.RESET +  "Nginx Version : ",Fore.RED,serverVersion)
    print(Fore.RESET)


def cvePrint(cveCounter,cveList):

    

    if cveCounter == 0:
        print(Fore.RED + "No CVE found!")
    else:
        print(Fore.LIGHTYELLOW_EX + "{}".format(cveCounter) ,Fore.RESET + "CVE Found !")
        print()

        for cve in cveList:
            print(Fore.LIGHTMAGENTA_EX+cve)
            print(Fore.RESET)

def detectionCVE(serverVersion):

    cveCounter = 0
    cveList = []

    for cveVersion in CVEs:

        if serverVersion == cveVersion:

            cveCounter += 1

            cveList.append(CVEs[cveVersion])

    serverPrint(serverVersion)
    cvePrint(cveCounter,cveList)

def serverParser(serverType):
    
    serverType = str(serverType)
    
    serverType = serverType.split("/")
    
    try:
        serverName = serverType[0]
        serverVersion = serverType[1]
    except IndexError:
        print(Fore.RED + "Server type is not Nginx !")
        exit()
    else:
        if serverName == "nginx":
            
            serverVersion = serverVersion.split(" ")
            serverVersion = serverVersion[0]

            detectionCVE(serverVersion)
            
            
        else:
            print(Fore.RED + "Server type is not Nginx !")
            exit()
def ip(IP):
    
    try:
        req = requests.get("http://{}".format(IP))
    except requests.exceptions.RequestException:
        print(Fore.RED + "The server is unreachable !")
        print(Fore.RED + "The server may not be reachable by IP. \n If so try again with the URL.")
        exit()
    
    
    serverType = req.headers.get("Server")

    if serverType == None:
        print(Fore.RED + "Server type cannot be determined")
        exit()
    else:
        serverParser(serverType)

def url(URL):
    
    try:
        req = requests.get(URL)
    except requests.exceptions.RequestException:
        print(Fore.RED + "The server is unreachable !")
        exit()
    
    
    serverType = req.headers.get("Server")

    if serverType == None:
        print(Fore.RED + "Server type cannot be determined")
        exit()
    else:
        serverParser(serverType)

def verify():
    try:
        
        IP = argv[1]
    except:
        if osName == "nt":
            winUsage()
        else:
            usage()
    try:
        ipCheck(IP)

    except ValueError:

        if not urlCheck(IP):
            if osName == "nt":
                winUsage()
            else:
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
        exit()
    except EOFError:
        print()
        print(Fore.LIGHTYELLOW_EX +"Logget out")
        exit()



