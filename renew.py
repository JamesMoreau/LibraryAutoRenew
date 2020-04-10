import webbrowser
import os

import wget
import zipfile
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
from win32com.client import Dispatch
from inscriptis import get_text
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    print("Auto renew has started")

    with open("user.txt") as f:
        username = f.readline().replace('\n', '')
        password = f.readline().replace('\n', '')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://ocul-gue.primo.exlibrisgroup.com/discovery/login?vid=01OCUL_GUE:GUELPH")

    # login type selection page
    driver.find_element_by_xpath('//*[@id="tab-content-0"]/div/md-content/md-list/md-list-item[1]/div/button').click()

    # uofg login page
    username_entry = driver.find_element_by_xpath('//*[@id="inputUsername"]')
    username_entry.clear()
    username_entry.send_keys(username)

    password_entry = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    password_entry.click()
    password_entry.send_keys(password)

    driver.find_element_by_xpath('//*[@id="main"]/article/form/div[4]/div/button').click()

    #omni main page
    driver.get('https://ocul-gue.primo.exlibrisgroup.com/discovery/account?vid=01OCUL_GUE:GUELPH&section=overview&lang=en')

    wait1 = WebDriverWait(driver, 10)
    first_result = wait1.until(presence_of_element_located((By.CSS_SELECTOR, "#tab-content-1 > div > div > div > prm-loans-overview > div > div > div > div > button")))
    first_result.click()