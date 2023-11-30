# Imports
import re
import logging
import os
import argparse

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from collections import defaultdict
from tqdm import tqdm

from notebooks.util import *

def main(debug, serialize):
    # Setup debugger
    if debug:
        setup_logger()
    if serialize:
        setup_serialize()

    # Pass in Selenium opts
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}]})
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features")
    options.add_argument('--disable-extensions')
    options.add_argument("--no-sandbox")
    options.binary_location = "/usr/local/bin/webdriver"
    driver = webdriver.Chrome(options=options)
    print("Internet connected: ", internet())

    # Generate names
    path = "./../data/pilot-names.json"
    white_female_names = generate_names(path, 'white', 'female')
    white_male_names = generate_names(path, 'white', 'male')
    black_female_names = generate_names(path, 'black', 'female')
    black_male_names = generate_names(path, 'black', 'male')
    all_names = {
        "wf": white_female_names,
        "wm": white_male_names,
        "bf": black_female_names,
        "bm": black_male_names
    }

    # Querying all names and obtaining the ads on the page (est. 4min)
    all_ads = [['Name', 'Group', 'Ad Domain', 'Ad Title', 'Ad Link']]
    for group, names in tqdm(all_names.items()):
        for name in tqdm(names):
            query = f"{name} public records"
            raw_html = bing_search(query, driver)
            
            # Serialize
            if serialize:
                with open(f'./html/{name.strip()}.html', 'w') as f:
                    f.write(raw_html)

            # Other res
            parsed = parse_bing_ads(raw_html, query)
            for domain, ad_items in parsed.items():
                for ad_opts in ad_items:
                    all_ads.append([name, group, domain, ad_opts[0], ad_opts[1]])

    with open('results.csv', 'w') as f:
        f.write(all_ads)
    

def setup_logger():
    # Setup logger
    if not os.path.exists('./logs/'):
        os.mkdir('./logs/')
    if not os.path.exists('./logs/bing-pilot.log'):
        open('./logs/bing-pilot.log', 'a').close()

    logging.basicConfig(
        filename='./logs/bing-pilot.log',
        filemode='w',
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.DEBUG
    )

def setup_serialize():
    # Setup logger
    if not os.path.exists('./html/'):
        os.mkdir('./html/')


def parse_bing_ads(raw_html, query):
    """ Parses the doman.TLD and the title, URL from the HTML
    """
    compiled = defaultdict(list)
    pattern = r'(?:http[s]?://)?(?:www\.)?([\w-]+\.[\w-]+)' # Matches the domain and TLD of a URL
    ads = BeautifulSoup(raw_html).select('.sb_add')
    for ad in ads:
        try:
            title = ad.select_one('h2').text
            link = ad.select_one('.b_adurl').text
            match = re.search(pattern, link)
            domain = match.group(1) if match else 'ERROR'
            compiled[domain].append((title, link))
        except Exception as e:
            logging.debug(f'Failed to parse ad HTML on query: {query}')
    return compiled

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Flags
    parser.add_argument("-d", "--debug", help="Writes to the log dir", action="store_true")
    parser.add_argument("-s", "--serialize", help="Serializes the raw HTML for ad hoc analysis", action="store_true")
    args = parser.parse_args()

    main(args.debug, args.serialize)