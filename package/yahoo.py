import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_yahoo(options, timkiem):
    # driver https://vn.yahoo.com/
    driver_yahoo = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_yahoo.get('https://vn.yahoo.com/')
    search_yahoo = driver_yahoo.find_element(By.CLASS_NAME, '_yb_ycegt')
    search_yahoo.send_keys(timkiem)
    search_yahoo.send_keys(Keys.ENTER)

    all_profile_url = []
    while True:
        time.sleep(8)
        page_source = BeautifulSoup(driver_yahoo.page_source, "html.parser")

        time.sleep(8)
        profiles = page_source.find_all("div", class_='algo')

        for profile in profiles:
            ID = profile.find('a', class_='d-ib').get('href')
            if ID not in all_profile_url:
                all_profile_url.append(ID)

        sleep(2)
        driver_yahoo.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(2)

        try:
            next_botton = driver_yahoo.find_element(By.CLASS_NAME, 'next')
            next_botton.click()
        except Exception as e:
            break

    driver_yahoo.close()
    return all_profile_url
