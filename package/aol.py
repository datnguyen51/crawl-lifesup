import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_aol(options, timkiem):
    # driver https://www.aol.com/
    driver_aol = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_aol.get('https://www.aol.com/')
    search_aol = driver_aol.find_element(By.CLASS_NAME, 'wafer-autocomplete')
    search_aol.send_keys(timkiem)
    search_aol.send_keys(Keys.ENTER)

    all_profile_url = []
    try:
        while True:
            time.sleep(10)
            page_source = BeautifulSoup(driver_aol.page_source, "html.parser")

            time.sleep(10)
            profiles = page_source.find_all("div", class_="algo-sr")

            for profile in profiles:
                ID = profile.find('a').get('href')
                if ID not in all_profile_url:
                    all_profile_url.append(ID)

            time.sleep(10)
            driver_aol.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(30)

            try:
                next_button = driver_aol.find_element(By.CLASS_NAME, 'next')
                next_button.click()
            except:
                break
    except:
        pass
    print('aol')
    driver_aol.close()
    return all_profile_url
