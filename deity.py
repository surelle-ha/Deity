# Developer: Harold Eustaquio(PHI)
# Language-Based: Python 3
# Framework: Deity
# Year: 2020
# Original Core Utility[DE]
import configparser
import pyfiglet
from os import system, name  
from os import walk
from coreutils import showd, coretext

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'                   

def dmagi(type, pkg):    
    if type == "install":
        print("")
    elif type == "remove":
        print("")
    else:
        raise TypeError()

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def dexit():
    exit()
 
#configuration parser   
config = configparser.ConfigParser()
config.read('usr/config.ini')
user = config['su']['user']
name = config['main']['name']
version = config['main']['version']
developer = config['main']['developer']
    
#banner        
result = pyfiglet.figlet_format(name)
print(bcolors.BOLD+bcolors.OKGREEN+result+bcolors.ENDC)
print(coretext.header)

#test array of packages
func_dict = {'dmagi':dmagi,'clear':clear,'dexit':dexit,'showd':showd}

while True:
    try:
        #PS1
        cmd = input(f'[{user}@{name}]$ ').split()
        func_dict[cmd[0]](*cmd[1:])
        
        if cmd[0] == "":
            continue
        elif cmd[0] == "exit":
            print(bcolors.WARNING+bcolors.BOLD+"[code:72] Exit.\n"+bcolors.ENDC)
            break
        else:
            print("")  
    except KeyError:
        etc = []
        for (dirpath, dirnames, filenames) in walk("etc/"):
            etc.extend(filenames)
            break
        if cmd[0]+".py" in etc:
            system('python etc/'+cmd[0]+'.py')
        else:
            print(bcolors.FAIL+bcolors.BOLD+"[code:90] Command ["+cmd[0]+"] Not Found.\n"+bcolors.ENDC)
    except TypeError:
        print(bcolors.WARNING+bcolors.BOLD+"[code:56] Invalid Syntax or Parameter for ["+cmd[0]+"].\n"+bcolors.ENDC)
    except IndexError:
        print("")