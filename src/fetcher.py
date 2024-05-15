# Apostolos Chalis 2024
# A script to fetch me the latest EOPEPP announcements 
import requests 
from colorama import Fore
from bs4 import BeautifulSoup
import argparse

eopepp_url = "https://www.eoppep.gr/index.php/el/announcements"

parser = argparse.ArgumentParser(
            prog="eopeppFetcher", 
            description="A script that fetches EOPEPP announcements to lower the risk of loosing your exams.",
            epilog="Author: Apostolos Chalis 2024 <achalis@acm.org>"
        )

parser.add_argument('-l', '--last', action='store_const', const = True, help="Last EOPEPP post")
parser.add_argument('-a', '--all', action='store_const', const = True, help="All EOPEPP posts (1st page only)")

args = parser.parse_args() 

try: 
    r = requests.get(eopepp_url)
    site_content = r.text
except: 
    print(f"{Fore.RED}ERROR:{Fore.WHITE} Could not reach EOPEPP site.")
    exit(0)

parsed_content = BeautifulSoup(site_content, 'html.parser')
# I am putting a limit because they load exactly 5 posts per page
titles_of_exams = parsed_content.find_all("h3", limit = 5)

if args.all == True and args.last == None: 
    for h3 in titles_of_exams: 
        print(h3.text.strip(), "\n") 

elif args.all == None and args.last == True: 
    for h3 in titles_of_exams: 
        print(h3.text.strip())
        break 
else: 
    print(f"{Fore.RED}ERROR:{Fore.WHITE} Wrong flag combination.")
