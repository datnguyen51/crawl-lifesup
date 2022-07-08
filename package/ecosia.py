import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_ecosia(options, timkiem):
    # driver https://www.ecosia.com/
    driver_ecosia = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_ecosia.get('https://www.ecosia.org/')
    search_ecosia = driver_ecosia.find_element(By.CLASS_NAME, 'search-form__input')
    search_ecosia.send_keys(timkiem)
    search_ecosia.send_keys(Keys.ENTER)

    all_profile_url = []
    while True:
        time.sleep(10)
        page_source = BeautifulSoup(driver_ecosia.page_source, "html.parser")

        time.sleep(10)
        profiles = page_source.find_all("a", class_="result__link")

        for profile in profiles:
            ID = profile.get('href')
            if ID not in all_profile_url:
                all_profile_url.append(ID)

        sleep(10)
        driver_ecosia.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(30)

        try:
            next_botton = driver_ecosia.find_element(By.CLASS_NAME, 'pagination-control-next')
            next_botton.click()
        except:
            break

    driver_ecosia.close()
    return all_profile_url
