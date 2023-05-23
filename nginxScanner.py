#! /usr/bin/python3

import requests
from ipaddress import ip_address as ipCheck
from validators import url as urlCheck
from colorama import Fore
from sys import argv,exit
from os import name as osName
from random import choice

def usage():
    print(Fore.LIGHTGREEN_EX + """
Usage: nginxScanner <IP> or <URL>

EXAMPLES:

nginxScanner 192.168.1.1
nginxScanner http://172.16.204.131/
nginxScanner https://example.com

    """)
    exit()

def winUsage():
    print(Fore.LIGHTGREEN_EX + """
Usage: python nginxScanner <IP> or <URL>

EXAMPLES:

python nginxScanner 192.168.1.1
python nginxScanner http://172.16.204.131/
python nginxScanner https://example.com

    """)
    exit()

def noCVE():
    print(Fore.RED + "No CVE Found !")
    quit()


def serverPrint(serverVersion):
    print(Fore.RESET + "Server : ",Fore.RED,argv[1])
    print(Fore.RESET +  "Nginx Version : ",Fore.RED,serverVersion)
    print(Fore.RESET)

def cvePrint(cveList,cveCount):
    if cveCount == 0:
        noCVE()
    else:
        print(Fore.LIGHTYELLOW_EX,cveCount,Fore.RESET, "CVE Found ! ")
        print()
        for cve in cveList:
            print(Fore.LIGHTMAGENTA_EX+cve)
            
            print()
            
        print()


def cveDetection(major,minor,micro):
    cveList = list()

    
# ----------------CVE-2022-41741 - START----------------
    
    if major == 1 and minor == 23 and micro == 1:
        cveList.append("CVE-2022-41741")
    elif major == 1 and minor < 23:
        if minor == 22 and micro >= 1:
            pass
        elif minor == 1 and micro >= 3:
            cveList.append("CVE-2022-41741")
        elif minor >= 1:
            cveList.append("CVE-2022-41741")
        elif minor == 0 and micro>=7 and micro <=15:
            cveList.append("CVE-2022-41741")
     
# ----------------CVE-2022-41741 - END ----------------

# ----------------CVE-2022-41742- START----------------
    if major == 1 and minor == 23 and micro == 1:
        cveList.append("CVE-2022-41742")
    elif major == 1 and minor < 23:
        if minor == 22 and micro >= 1:
            pass
        elif minor == 1 and micro >= 3:
            cveList.append("CVE-2022-41742")
        elif minor >= 1:
            cveList.append("CVE-2022-41742")
        elif minor == 0 and micro>=7 and micro <=15:
            cveList.append("CVE-2022-41742")
    

# ----------------CVE-2022-41742- END----------------

# ----------------CVE-2021-23017- START----------------
    if major == 1 and minor == 20 and micro == 0:
        cveList.append("CVE-2021-23017")
    elif major == 1:
        if minor < 20:
            cveList.append("CVE-2021-23017")
    elif major == 0:
        if minor == 6 and micro == 18:
            cveList.append("CVE-2021-23017")
        elif minor >= 6:
            cveList.append("CVE-2021-23017")
    

# ----------------CVE-2021-23017- END----------------


# ----------------CVE-2019-9511- START----------------
    if major == 1 and minor == 17 and (micro == 2 or micro == 1):
        cveList.append("CVE-2019-9511")
    elif major == 1 and minor <= 17 and minor >= 9:
        if minor == 9 and micro >= 5:
            cveList.append("CVE-2019-9511")
        else:
            cveList.append("CVE-2019-9511")

# ----------------CVE-2019-9511- END----------------

    else:
        pass

    cveCount = len(cveList)

    cvePrint(cveList,cveCount)

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

            serverPrint(serverVersion)

            serverVersion = serverVersion.split(".")
            
            major = int(serverVersion[0])
            minor = int(serverVersion[1])
            micro = int(serverVersion[2])

            cveDetection(major,minor,micro)
            
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

def banner2():
    banner =Fore.CYAN +"""
WWNNWWWNNNWWNNWWWNNNWN0xoodOXNWWWNNNWWNNWWWNNWWWNN
NNNNNNNNWWNNNWWWNNKkd:'....';lkKNWNNWWNNWNWWWWNNNN
NNWWNNNWWWNNWWXOdl;............,cx0XNNWWWNNWWWNNWW
WWNNWWWNNNWNOo:'..''..........''..':oOKNNWWNNNWWNN
NNWWWNNWWWNx,...,dK0xc'......:kOo'...,xWWNNWWWNNWW
WWNNWWWNNWWk,...;ONWWXx;.....oXWO;...'dNNWWNNWWWNN
NWWWWWWNWWNx'...;0NNKKNKo:'..oXWO;...'dNNNWWNWWWWW
NNWWWNNWWWNx'...;0WXl:kNNKOc'oXNO;...'xNWNNWWWNNWW
WWNNWWWNNWWk,...:ONXl.'c0NNXkkNWO;...'dXWWWNNWWWNN
NNWWNNNWWWNx'...:0WXl...,:oKWWNNk;...'xWWNNWWWNNWW
WWNNWWWNNNWk'...;kNKc......:xKNNk,...'dNWWWNNWWWNN
NNNNNNWNWWN0o;'..;c:'.......';cc;...,l0NNWNNNWNNNW
NNWWWNNWWNNNNXOd:'..............':okKNWWNNNWWNNNWW
WWNNNWWNNWWWNNWWN0xc;........,cx0KXWWWNNNWWNNWWWNN
NNWWNNNWWWNNWWNNNWMN0ko:,,;lkXNNNWWWNNWWWXNWWNNNWW
                   
{}          TURKZEN & OzlemBalci
{}      github.com/TURKZEN/nginxScanner
    """.format(Fore.LIGHTMAGENTA_EX,Fore.LIGHTCYAN_EX )
    
    print(banner)

def banner3():
    banner = Fore.LIGHTYELLOW_EX + """
_  _ ____ _ _  _ _  _ ____ ____ ____ _  _ _  _ ____ ____ 
|\ | | __ | |\ |  \/  [__  |    |__| |\ | |\ | |___ |__/ 
| \| |__] | | \| _/\_ ___] |___ |  | | \| | \| |___ |  \ 
                                                         
{}              TURKZEN & OzlemBalci                                                   
{}          github.com/TURKZEN/nginxScanner
    """.format(Fore.LIGHTCYAN_EX,Fore.GREEN)
    print(banner)

def randomBanner():
    bannerList = [1,2,3]
    bannerChoice = choice(bannerList)
    
    if bannerChoice == 1:
        banner()
    elif bannerChoice == 2:
        banner2()
    elif bannerChoice == 3:
        banner3()
    else:
        pass

def Main():
    randomBanner()
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



