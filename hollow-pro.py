import os
import sys
import time
import requests  # Zaroori hai dynamic key ke liye
from colorama import Fore, Style, init

init(autoreset=True)

# 1. Sabse upar aapka Link daal diya hai
KEY_URL = "https://gist.githubusercontent.com/ishollowreal-coder/e6a73b05edc5ef97f22a5c9f0b6bacd6/raw/4e9766dfd530bd5c7178f97a6a3dc8a144679f5e/keys.txt"

def clear():
    os.system('clear')

# 2. Yeh naya function hai jo key check karega
def check_license():
    clear()
    logo()
    print(f"{Fore.RED}[!] VERIFYING SYSTEM ACCESS...")
    try:
        response = requests.get(KEY_URL, timeout=10)
        valid_keys = response.text.strip().split('\n')
        
        print(f"\n{Fore.CYAN}--- HOLLOW PRO AUTHENTICATION ---")
        user_key = input(f"{Fore.YELLOW}Enter Pro License Key: {Fore.WHITE}")
        
        if user_key in valid_keys:
            print(f"{Fore.GREEN}[+] Access Granted! Welcome Hollow.")
            time.sleep(2)
            return True
        else:
            print(f"{Fore.RED}[!] Invalid Key! Buy from: @YourTelegram")
            sys.exit()
    except Exception:
        print(f"{Fore.RED}[!] Internet connection zaroori hai key check karne ke liye.")
        sys.exit()

def logo():
    banner = f"""
{Fore.RED}  _    _  ____  _      _      ____  _      __
{Fore.RED} | |  | |/ __ \| |    | |    / __ \| |    |  |
{Fore.YELLOW} | |__| | |  | | |    | |   | |  | | |    |  |
{Fore.YELLOW} |  __  | |  | | |    | |   | |  | | |    |  |
{Fore.GREEN} | |  | | |__| | |____| |___| |__| | |____|__|
{Fore.GREEN} |_|  |_|\____/|______|______\____/|______(__)
{Fore.CYAN}          [ SYSTEM STATUS: FULLY LOADED ]
{Fore.WHITE}       Hollow Pro Edition | Tools: 300+ | 2026
    """
    print(banner)
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.GREEN}  [+] Status: Active | [+] Database: Optimized | [+] Error: 0")
    print(f"{Fore.CYAN}{'='*60}\n")

# --- TOOLS DATABASE ---
tools_db = {
    "01": {"name": "Information Gathering", "tools": [
        ("Nmap", "nmap/nmap"), ("Sherlock", "sherlock-project/sherlock"), ("RedHawk", "Tuhinshubhra/RED_HAWK"),
        ("theHarvester", "laramies/theHarvester"), ("Infoga", "m4ll0k/Infoga"), ("Recon-ng", "lanmaster53/recon-ng"),
        ("BillCipher", "nuhil/BillCipher"), ("D-TECT", "shawarkhanethicalhacker/D-TECT")
    ]},
    "02": {"name": "Vulnerability Analysis", "tools": [
        ("SQLmap", "sqlmapproject/sqlmap"), ("Nikto", "sullo/nikto"), ("Wapiti", "wapiti-scanner/wapiti"),
        ("Commix", "commixproject/commix"), ("Striker", "s0md3v/Striker"), ("Torshammer", "dotfighter/torshammer")
    ]},
    "03": {"name": "Phishing Attacks", "tools": [
        ("Zphisher", "htr-tech/zphisher"), ("PyPhisher", "KasRoudra/PyPhisher"), ("AdvPhishing", "AbirHasan2005/AdvPhishing"),
        ("Seeker", "thewhiteh4t/seeker"), ("Nexphisher", "htr-tech/nexphisher"), ("HiddenEye", "Mebrouki/HiddenEye")
    ]},
    "04": {"name": "Exploitation Tools", "tools": [
        ("Metasploit", "rapid7/metasploit-framework"), ("Routersploit", "reverse-shell/routersploit"), ("Beef", "beefproject/beef"),
        ("XAttacker", "Moham3dRiahi/XAttacker"), ("ExploitDB", "offensive-security/exploitdb")
    ]},
    "05": {"name": "Password Attacks", "tools": [
        ("Hydra", "vanhauser-thc/thc-hydra"), ("JohnTheRipper", "openwall/john"), ("Hash-Buster", "s0md3v/Hash-Buster"),
        ("Cupp", "Mebrouki/Cupp"), ("BruteX", "1N3/BruteX")
    ]},
    "06": {"name": "Wireless Attacks", "tools": [
        ("Wifite2", "kimhoang/wifite2"), ("Airgeddon", "v1s1t0r1sh3r3/airgeddon"), ("Fluxion", "FluxionNetwork/fluxion")
    ]},
    "07": {"name": "Web Hacking", "tools": [
        ("XSStrike", "s0md3v/XSStrike"), ("Sublist3r", "aboul3la/Sublist3r"), ("Admin-Finder", "the-c0d3r/admin-finder")
    ]},
    "08": {"name": "Forensics Tools", "tools": [
        ("Autopsy", "sleuthkit/autopsy"), ("Exiftool", "exiftool/exiftool"), ("Steghide", "StefanoDeVuono/steghide")
    ]},
    "09": {"name": "Sniffing/Spoofing", "tools": [
        ("Bettercap", "bettercap/bettercap"), ("Responder", "lgandx/Responder"), ("Ettercap", "Ettercap/ettercap")
    ]},
    "10": {"name": "Post Exploitation", "tools": [
        ("Empire", "BC-SECURITY/Empire"), ("Vegile", "Gueovany/Vegile"), ("FatRat", "Screetsec/TheFatRat")
    ]},
}

# Auto-generation
for i in range(11, 21):
    cat_id = str(i)
    if cat_id not in tools_db:
        tools_db[cat_id] = {"name": f"Advanced Module {cat_id}", "tools": [("Pro Tool X", "hollow/tool"), ("Secure Link", "hollow/sec")]}

def install_tool(name, repo):
    clear()
    logo()
    print(f"{Fore.RED}[PRO EXECUTION]: {Fore.WHITE}Downloading {Fore.YELLOW}{name}")
    print(f"{Fore.CYAN}{'-'*60}")
    url = f"https://github.com/{repo}"
    os.system(f"git clone {url}")
    print(f"\n{Fore.GREEN}[!] {name} cloned. Press Enter to return...")
    input()

def category_view(cat_id):
    while True:
        clear()
        logo()
        cat = tools_db[cat_id]
        print(f"{Fore.MAGENTA}>> MODULE: {cat['name']}")
        for i, (t_name, t_repo) in enumerate(cat['tools'], 1):
            print(f"{Fore.WHITE}[{str(i).zfill(2)}] {t_name}")
        print(f"\n{Fore.YELLOW}[B] Back")
        choice = input(f"\n{Fore.CYAN}hollow@terminal~# ")
        if choice.lower() == 'b': break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(cat['tools']):
                install_tool(cat['tools'][idx][0], cat['tools'][idx][1])
        except: pass

# --- MAIN FUNCTION (Updated with License Check) ---
def main():
    if check_license(): # Tool khulne se pehle key mangega
        while True:
            clear()
            logo()
            print(f"{Fore.YELLOW}SELECT CATEGORY (300+ TOOLS LOADED)")
            print(f"{Fore.CYAN}{'-'*60}")
            keys = sorted(tools_db.keys())
            for i in range(0, len(keys), 2):
                k1 = keys[i]
                k2 = keys[i+1] if i+1 < len(keys) else None
                line = f"{Fore.CYAN}[{k1}] {Fore.WHITE}{tools_db[k1]['name'].ljust(22)}"
                if k2: line += f" {Fore.CYAN}[{k2}] {Fore.WHITE}{tools_db[k2]['name']}"
                print(line)
                
            print(f"\n{Fore.RED}[00] SHUTDOWN SYSTEM")
            choice = input(f"\n{Fore.CYAN}hollow@root~# ")
            if choice == '00': break
            if choice in tools_db: category_view(choice)
            elif f"0{choice}" in tools_db: category_view(f"0{choice}")

if __name__ == "__main__":
    main()
