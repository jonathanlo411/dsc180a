
# --- Imports ---
import socket
import json
from selenium import webdriver

# --- Helpers ---

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

class CAPTCHAException(Exception):
    pass

def bing_search(query, driver):
    if internet():
        try:
            url = f"https://www.bing.com/search?q={query}"
            driver.get(url)
            if len(driver.page_source) < 100000:
                raise CAPTCHAException
            else:
                return driver.page_source
        except CAPTCHAException:
            print("CAPTCHA detected!")
            return driver.page_source
    else:
        print("No internet")
        return None
    
def google_search(query, driver):
    if internet():
        try:
            url = f"https://www.google.com/search?q={query}"
            driver.get(url)
            if len(driver.page_source) < 100000:
                raise CAPTCHAException
            else:
                return driver.page_source
        except CAPTCHAException:
            print("CAPTCHA detected!")
            return driver.page_source
    else:
        print("No internet")
        return None
    
def generate_names(data_path, race, sex):
    names = list()
    names_data = json.load(open(data_path, "r"))
    for first_name in names_data[race]['first'][sex]:
        for last_name in names_data[race]['last']:
            names.append(f"{first_name} {last_name}")
    return names

def flatten(l):
    return [item for sublist in l for item in sublist]