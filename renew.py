import webbrowser
import wget
import zipfile
import urllib.request
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from win32com.client import Dispatch
from inscriptis import get_text

def update_chrome_driver(chrome_version):
    print("UPDATING CHROME DRIVER.")
    x = chrome_version.split(".")
    del x[-1]
    y = '.'.join(x)

    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + y

    html = urllib.request.urlopen(url).read().decode('utf-8')
    text = get_text(html)
    driver_version_needed = text.replace('\n', '')

    driver_file_url = 'https://chromedriver.storage.googleapis.com/' + driver_version_needed + '/chromedriver_win32.zip' 
    filepath = wget.download(driver_file_url, "ChromeDrivers/")
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall("ChromeDrivers")

    os.remove(filepath) # remove zip files 





def get_version_via_com(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

if __name__ == "__main__":
    paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
             r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
    print(version)

    update_chrome_driver(version) # this should be used as an exception if the current driver is out of date