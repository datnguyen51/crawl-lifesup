import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_ask(options, timkiem):
    # driver https://www.ask.com/
    driver_ask = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_ask.get('https://www.ask.com/')
    search_ask = driver_ask.find_element(By.CLASS_NAME, 'search-box')
    search_ask.send_keys(timkiem)
    search_ask.send_keys(Keys.ENTER)

    all_profile_url = []
    while True:
        time.sleep(20)
        page_source = BeautifulSoup(driver_ask.page_source, "html.parser")

        time.sleep(10)
        profiles = page_source.find_all("a", class_="Link_theme_normal")
        print(profiles)

        for profile in profiles:
            ID = profile.get('href')
            if ID not in all_profile_url:
                all_profile_url.append(ID)

        sleep(10)
        driver_ask.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(20)

        try:
            next_botton = driver_ask.find_element(By.CLASS_NAME, 'pager__item_kind_next')
            next_botton.click()
        except:
            break

    driver_ask.close()
    return all_profile_url
