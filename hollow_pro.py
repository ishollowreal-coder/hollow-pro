import os
import sys
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

# --- CONFIG ---
# Aapka original Gist Raw Link
KEY_URL = "https://gist.githubusercontent.com/ishollowreal-coder/e6a73b05edc5ef97f22a5c9f0b6bacd6/raw/4e9766dfd530bd5c7178f97a6a3dc8a144679f5e/keys.txt"

def clear():
    os.system('clear')

def check_license():
    clear()
    # Ek simple loading effect professional look ke liye
    print(f"{Fore.CYAN}[*] Connecting to Hollow Server...")
    try:
        response = requests.get(KEY_URL, timeout=10)
        valid_keys = response.text.strip().split('\n')
        
        print(f"\n{Fore.WHITE}--- {Fore.RED}SECURITY VERIFICATION {Fore.WHITE}---")
        user_key = input(f"{Fore.GREEN}Enter Your License Key: {Fore.WHITE}").strip()
        
        if user_key in valid_keys:
            print(f"\n{Fore.GREEN}[SUCCESS] Access Granted. Authenticating...")
            time.sleep(2)
            return True
        else:
            print(f"\n{Fore.RED}[ERROR] Invalid Key!")
            print(f"{Fore.YELLOW}Contact Hollow to get a valid key.")
            sys.exit()
    except Exception:
        print(f"\n{Fore.RED}[!] ERROR: No Internet Connection.")
        print("This tool requires an active connection to verify the key.")
        sys.exit()

def logo():
    banner = f"""
{Fore.RED}  _    _  ____  _      _      ____  _      __
{Fore.RED} | |  | |/ __ \| |    | |    / __ \| |    |  |
{Fore.YELLOW} | |__| | |  | | |    | |   | |  | | |    |  |
{Fore.YELLOW} |  __  | |  | | |    | |   | |  | | |    |  |
{Fore.GREEN} | |  | | |__| | |____| |___| |__| | |____|__|
{Fore.GREEN} |_|  |_|\____/|______|______\____/|______(__)
{Fore.WHITE}       Hollow Pro Edition | Tools: 300+ | 2026
    """
    print(banner)
    print(f"{Fore.YELLOW}{'='*60}")
    print(f"{Fore.GREEN}  Status: ACTIVE | User: PRO | Dev: Hollow")
    print(f"{Fore.YELLOW}{'='*60}\n")

# Database (Functional for Categories 01-10)
tools_db = {
    "01": {"name": "Information Gathering", "tools": [("Nmap", "nmap/nmap"), ("Sherlock", "sherlock-project/sherlock")]},
    "02": {"name": "Vulnerability Analysis", "tools": [("SQLmap", "sqlmapproject/sqlmap"), ("Nikto", "sullo/nikto")]},
    "03": {"name": "Phishing Attacks", "tools": [("Zphisher", "htr-tech/zphisher"), ("PyPhisher", "KasRoudra/PyPhisher")]},
    "04": {"name": "Exploitation Tools", "tools": [("Metasploit", "rapid7/metasploit-framework"), ("Beef", "beefproject/beef")]},
    "05": {"name": "Password Attacks", "tools": [("Hydra", "vanhauser-thc/thc-hydra"), ("JohnTheRipper", "openwall/john")]},
    "06": {"name": "Wireless Attacks", "tools": [("Wifite2", "kimhoang/wifite2"), ("Fluxion", "FluxionNetwork/fluxion")]},
    "07": {"name": "Web Hacking", "tools": [("XSStrike", "s0md3v/XSStrike"), ("Sublist3r", "aboul3la/Sublist3r")]},
    "08": {"name": "Forensics Tools", "tools": [("Autopsy", "sleuthkit/autopsy"), ("Steghide", "StefanoDeVuono/steghide")]},
    "09": {"name": "Sniffing/Spoofing", "tools": [("Bettercap", "bettercap/bettercap"), ("Responder", "lgandx/Responder")]},
    "10": {"name": "Post Exploitation", "tools": [("Empire", "BC-SECURITY/Empire"), ("FatRat", "Screetsec/TheFatRat")]},
}

# Auto-Filler for Categories 11-20
for i in range(11, 21):
    cat_id = str(i)
    if cat_id not in tools_db:
        tools_db[cat_id] = {"name": f"Module {cat_id} (PRO)", "tools": [("Special Tool", "hollow/special")]}

def install_tool(name, repo):
    clear()
    logo()
    print(f"{Fore.BLUE}[INSTALLING]: {Fore.WHITE}{name}")
    os.system(f"git clone https://github.com/{repo}")
    input(f"\n{Fore.GREEN}[+] Process Finished. Press Enter...")

def category_view(cat_id):
    while True:
        clear()
        logo()
        cat = tools_db[cat_id]
        print(f"{Fore.MAGENTA}>> MODULE: {cat['name']}")
        for i, (t_name, t_repo) in enumerate(cat['tools'], 1):
            print(f"{Fore.CYAN}[{i}] {Fore.WHITE}{t_name}")
        print(f"\n{Fore.YELLOW}[B] Back")
        choice = input(f"\n{Fore.CYAN}hollow@terminal~# ")
        if choice.lower() == 'b': break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(cat['tools']):
                install_tool(cat['tools'][idx][0], cat['tools'][idx][1])
        except: pass

def main():
    if check_license():
        while True:
            clear()
            logo()
            keys = sorted(tools_db.keys())
            for i in range(0, len(keys), 2):
                k1 = keys[i]
                k2 = keys[i+1] if i+1 < len(keys) else None
                line = f"{Fore.CYAN}[{k1}] {Fore.WHITE}{tools_db[k1]['name'].ljust(22)}"
                if k2: line += f" {Fore.CYAN}[{k2}] {Fore.WHITE}{tools_db[k2]['name']}"
                print(line)
            print(f"\n{Fore.RED}[00] EXIT")
            choice = input(f"\n{Fore.CYAN}hollow@root~# ")
            if choice == '00': break
            if choice in tools_db: category_view(choice)
            elif f"0{choice}" in tools_db: category_view(f"0{choice}")

if __name__ == "__main__":
    main()
      
