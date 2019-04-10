import os
import time
from sources import *
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    
print ('\033[94m[1] for kali')
print ('\033[94m[2] for termux')
tool = input('protocol ==> ')
if tool == "1" or tool == "01":
     kali_user()
     
elif tool == "2" or tool == "02":
     termux_user()
     save_free()
     auto()
     
