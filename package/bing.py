import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_bing(options, timkiem):
    # driver https://www.bing.com/
    driver_bing = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_bing.get('https://www.bing.com/')
    search_bing = driver_bing.find_element(By.CLASS_NAME, 'sb_form_q')
    search_bing.send_keys(timkiem)
    search_bing.send_keys(Keys.ENTER)

    all_profile_url = []
    try:
        while True:
            time.sleep(10)
            page_source = BeautifulSoup(driver_bing.page_source, "html.parser")

            time.sleep(10)
            profiles = page_source.find_all("li", class_="b_algo")

            for profile in profiles:
                ID = profile.find('a').get('href')
                if ID not in all_profile_url:
                    all_profile_url.append(ID)

            time.sleep(20)
            driver_bing.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(20)

            try:
                next_button = driver_bing.find_element(By.CLASS_NAME, 'sb_pagN')
                if next_button.get_attribute('href'):
                    next_button.click()
                else:
                    break
            except:
                break
    except:
        pass
    print('bing')
    driver_bing.close()
    return all_profile_url
