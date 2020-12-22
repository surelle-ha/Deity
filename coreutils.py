from os import system, name  
from os import walk

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

def showd(dir = "./"):
    etc = []
    for (dirpath, dirnames, filenames) in walk(dir):
        etc.extend(filenames)
        break
    for x in range(len(etc)):
        print(bcolors.OKCYAN+etc[x]+bcolors.ENDC), 
        
class coretext():
    header = bcolors.BOLD+bcolors.OKGREEN+"""
Welcome to Deity Framework!
Developer: Harold Eustaquio
==========================================
Dev  Status: Active
Operating System Based: Linux
Programming Language: Python3 
==========================================   
Install a package: dmagi install <package>
More  information: dmagi info <package>
Search   package: dmagi search <package>
Update package: dmagi update <package>
==========================================  
Chat:  https://discord.gg/wyvuR9X79W
Forum: http://forestfiend.cf
Help: info query and man query   
    """+bcolors.ENDC
