import time
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    print("Auto renew has started")

    with open("user.txt") as f: #text file containing username and password required.
        username = f.readline().replace('\n', '')
        password = f.readline().replace('\n', '')

    # make headless browser
    # options = Options()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get("https://ocul-gue.primo.exlibrisgroup.com/discovery/login?vid=01OCUL_GUE:GUELPH")
    print("Primo page")
    time.sleep(5)

    # login type selection page
    el = driver.find_element_by_xpath('//*[@id="tab-content-0"]/div/md-content/md-list/md-list-item[1]/div/button')
    actions = ActionChains(driver)
    actions.move_to_element(el).click().perform()

    time.sleep(5)

    # uofg login page
    username_entry = driver.find_element_by_xpath('//*[@id="inputUsername"]')
    username_entry.clear()
    username_entry.send_keys(username)
    password_entry = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    password_entry.click()
    password_entry.send_keys(password)
    print("logged in to UofG redirect")

    time.sleep(5)

    driver.find_element_by_xpath('//*[@id="main"]/article/form/div[4]/div/button').click()
    
    time.sleep(5)

    #omni main page
    driver.get('https://ocul-gue.primo.exlibrisgroup.com/discovery/account?vid=01OCUL_GUE:GUELPH&section=overview&lang=en')
    print("On omni dashboard")
    time.sleep(5)
    renew_button = driver.find_element_by_xpath('//*[@id="tab-content-4"]/div/div/div/prm-loans-overview/div/div/div/div/button').click()
    print("Successfully renewed all book loans!")

    driver.close()