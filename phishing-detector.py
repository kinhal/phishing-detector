import requests
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)

def print_title():
    title = r"""
  ____  _     _     _           _               
 |  _ \| |__ (_)___| |__   ___ | | _____ _ __   
 | |_) | '_ \| / __| '_ \ / _ \| |/ / _ \ '__|  
 |  __/| | | | \__ \ | | | (_) |   <  __/ |     
 |_|   |_| |_|_|___/_| |_|\___/|_|\_\___|_|     
                                               
        --- PHISHING PAGE DETECTOR ---
    """
    print(Fore.CYAN + title + Style.RESET_ALL)

def check_ssl(url):
    try:
        r = requests.get(url, timeout=8)
        if r.url.startswith("https://"):
            return True
        else:
            return False
    except requests.exceptions.SSLError:
        return False
    except requests.exceptions.RequestException:
        return False

def suspicious_keywords(url):
    keywords = ['login', 'secure', 'account', 'update', 'free', 'verify', 'bank', 'confirm', 'webscr', 'paypal', 'signin']
    url_lower = url.lower()
    found = [kw for kw in keywords if kw in url_lower]
    return found

def main():
    print_title()
    url = input(Fore.GREEN + "Enter URL to check: " + Style.RESET_ALL).strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        print(Fore.RED + "Error: URL must start with http:// or https://")
        return

    print(Fore.YELLOW + "\n[+] Checking SSL certificate..." + Style.RESET_ALL)
    ssl_ok = check_ssl(url)
    if ssl_ok:
        print(Fore.GREEN + "  SSL certificate seems valid (HTTPS connection).\n")
    else:
        print(Fore.RED + "  SSL certificate missing or invalid!\n")

    print(Fore.YELLOW + "[+] Checking suspicious keywords in URL..." + Style.RESET_ALL)
    suspicious = suspicious_keywords(url)
    if suspicious:
        print(Fore.RED + f"  Suspicious keywords found: {', '.join(suspicious)}")
    else:
        print(Fore.GREEN + "  No suspicious keywords found.")

    print(Fore.YELLOW + "\n[!] Warning: This is a basic check and does NOT guarantee safety.\n" + Style.RESET_ALL)
    input(Fore.GREEN + "Press any key to exit..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
