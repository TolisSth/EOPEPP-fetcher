# Apostolos Chalis 2024
# A script to fetch me the latest EOPEPP announcements 
import requests 
from bs4 import BeautifulSoup
import argparse

eopepp_url = "https://www.eoppep.gr/index.php/el/announcements"

parser = argparse.ArgumentParser(
            prog="eopeppFetcher", 
            description="A script that fetches EOPEPP announcements to lower the risk of loosing your exams.",
            epilog="Author: Apostolos Chalis 2024 <achalis@acm.org>"
        )

parser.add_argument('-l', '--last', action='store_const', const = True, help="Last EOPEPP post")     # Last announcement
parser.add_argument('-a', '--all', action='store_const', const = True, help="All EOPEPP posts (1st page only)")      # Every announcement

args = parser.parse_args() 

