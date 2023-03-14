import argparse
import subprocess

# Color codes for text styling
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

def print_banner():
    print(BOLD + BLUE + '''

     )                     (                                  
  ( /(                     )\ )                 )             
  )\())   (          (    (()/( (            ( /(    )     )  
 ((_)\   ))\  `  )   )\ )  /(_)))\ )   (     )\())( /(  ( /(  
__ ((_) /((_) /(/(  (()/( (_)) (()/(   )\ ) (_))/ )(_)) )\()) 
\ \ / /(_))( ((_)_\  )(_))/ __| )(_)) _(_/( | |_ ((_)_ ((_)\  
 \ V / | || || '_ \)| || |\__ \| || || ' \))|  _|/ _` |\ \ /  
  |_|   \_,_|| .__/  \_, ||___/ \_, ||_||_|  \__|\__,_|/_\_\  
             |_|     |__/       |__/                          

 All in One Subdomain Finder Tool
 Builder by YupySyntax

''' + RESET)

def main(domain):
    # Print banner
    print_banner()

    # Sublist3r
    print(BOLD + GREEN + "\n[+] Running Sublist3r..." + RESET)
    subprocess.call(["sublist3r", "-d", domain, "-o", "output.txt"])
    with open("output.txt") as sublist3r_file:
        sublist3r = sublist3r_file.read().splitlines()
    print(BOLD + GREEN + "[+] Sublist3r finished!" + RESET)

    # Amass
    print(BOLD + YELLOW + "\n[+] Running Amass..." + RESET)
    subprocess.call(["amass", "enum", "-d", domain, "-o", "output.txt"])
    with open("output.txt") as amass_file:
        amass = amass_file.read().splitlines()
    print(BOLD + YELLOW + "[+] Amass finished!" + RESET)

    # Subfinder
    print(BOLD + BLUE + "\n[+] Running Subfinder..." + RESET)
    subprocess.call(["subfinder", "-d", domain, "-o", "output.txt"])
    with open("output.txt") as subfinder_file:
        subfinder = subfinder_file.read().splitlines()
    print(BOLD + BLUE + "[+] Subfinder finished!" + RESET)

    # Assetfinder
    print(BOLD + GREEN + "\n[+] Running Assetfinder..." + RESET)
    subprocess.call(["assetfinder", "-subs-only", domain, "-o", "output.txt"])
    with open("output.txt") as assetfinder_file:
        assetfinder = assetfinder_file.read().splitlines()
    print(BOLD + GREEN + "[+] Assetfinder finished!" + RESET)

    # Knockpy
    print(BOLD + YELLOW + "\n[+] Running Knockpy..." + RESET)
    subprocess.call(["knockpy", domain, "-o", "output.txt"])
    with open("output.txt") as knockpy_file:
        knockpy = knockpy_file.read().splitlines()
    print(BOLD + YELLOW + "[+] Knockpy finished!" + RESET)

    # Combine results and write to output file
    subdomains = set(sublist3r + amass + subfinder + assetfinder + knockpy)
    with open("hasil.txt", "w") as output_file:
        output_file.write("\n".join(subdomains))
    print(BOLD + GREEN + "\n[+] Results saved to hasil.txt!" + RESET)

if __name__ == '__main__':
    # Command line arguments
    parser = argparse.ArgumentParser(description=BOLD + 'All in One Subdomain Finder Tool' + RESET)
    parser.add_argument('domain', help=BOLD + 'example: yupysubdo.py domain.com' + RESET)
    args = parser.parse_args()

    # Run the main function
    main(args.domain)
