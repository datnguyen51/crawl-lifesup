import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_yandex(options, timkiem):
    # driver https://www.yandex.com/
    driver_yandex = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_yandex.get('https://www.yandex.com/')
    search_yandex = driver_yandex.find_element(By.CLASS_NAME, 'input__control')
    search_yandex.send_keys(timkiem)
    search_yandex.send_keys(Keys.ENTER)

    all_profile_url = []
    while True:
        time.sleep(8)
        page_source = BeautifulSoup(driver_yandex.page_source, "html.parser")

        time.sleep(8)
        profiles = page_source.find_all("a", class_="Link_theme_normal")

        for profile in profiles:
            ID = profile.get('href')
            if ID not in all_profile_url:
                all_profile_url.append(ID)

        sleep(2)
        driver_yandex.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(2)

        try:
            next_botton = driver_yandex.find_element(By.CLASS_NAME, 'pager__item_kind_next')
            next_botton.click()
        except:
            break

    driver_yandex.close()
    return all_profile_url
