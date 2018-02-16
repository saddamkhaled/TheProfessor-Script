import socket,os,re,subprocess
import urllib.request,json
import sys
from datetime import datetime
from json import load

print("\033[1;32;48m\n"
      "\n  ________                             __                                         _       _"
      "\n|__   __| |                           / _|                                       (_)     | |"
      "\n  | |  | |__   ___   _ __  _ __ ___ | |_ ___  ___ ___  ___  _ __   ___  ___ _ __ _ _ __ | |_"
      "\n | |  | '_ \ / _ \ | '_ \| '__/ _ \|  _/ _ \/ __/ __|/ _ \| '__| / __|/ __| '__| | '_ \| __|"
      "\n | |  | | | |  __/ | |_) | | | (_) | ||  __/\__ \__ \ (_) | |    \__ \ (__| |  | | |_) | |_"
      "\n |_|  |_| |_|\___| | .__/|_|  \___/|_| \___||___/___/\___/|_|    |___/\___|_|  |_| .__/ \__|"
      "\n                | |                                                           | |"
      "\n               |_|                                                           |_|"
)
str=(
    "\n=============================================================================="
    "\ntitle           :TPS-script.py                                               ="
    "\ndescription	    :TheProfessor-Scanner script will show your internal IP"
    "\n                 and your Public IP.Then you can scan any host your in your"
    "\n                 network to enumerate the opened ports. "
                      
    "\nauthor			:Saddam ben khaled                                           ="
    "\ndate			:2018-02-10                                                  ="
    "\nversion		    :1.0                                                         ="   
    "\nusage			:python TPS-script.py                                        ="
    "\nnotes			:Of course a good \"coder\" has to be able to write code"
    "\n                 from scratch! copying the code will not make you a coder ;) ="
    "\npython_version	:3.6                                                         ="
    "\n=============================================================================="
    )
print(str)

def myip():
            print("\n  Your internal IP adresse is :  ")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            inip=s.getsockname()[0]
            print("\033[1;31m ",inip,"\033[1;m")
            print("\033[1;32;48m\n--------------------------------")
            s.close()
            print("\033[1;32;48m\n  Your public IP adresse is : ")
            my_pip = urllib.request.urlopen('http://jsonip.com').read()
            jsonr = json.loads(my_pip.decode("utf-8"))
            print(" \033[1;31m",jsonr['ip'],"\033[1;m ")
            print("\033[1;32;48m\n--------------------------------")


print(myip())

def PortScan():
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)
    t1 = datetime.now()
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
    t2 = datetime.now()
    total = t2 - t1
    print('Scanning Completed in: ', total)
def selection():


    choice = input(

        "\n1-Scan Host for opened ports "
        "\nPlease select your choice:")
    for choice in (1,2):
        if choice == 1:
         print(PortScan())


print(selection())



