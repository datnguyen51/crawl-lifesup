import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_duckduckgo(options, timkiem):
    # driver https://www.duckduckgo.com/
    driver_duckduckgo = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_duckduckgo.get('https://www.duckduckgo.com/')
    search_duckduckgo = driver_duckduckgo.find_element(By.CLASS_NAME, 'js-search-input')
    search_duckduckgo.send_keys(timkiem)
    search_duckduckgo.send_keys(Keys.ENTER)

    all_profile_url = []
    try:
        while True:
            time.sleep(10)
            page_source = BeautifulSoup(driver_duckduckgo.page_source, "html.parser")

            time.sleep(10)
            profiles = page_source.find_all("a", class_="Rn_JXVtoPVAFyGkcaXyK")

            for profile in profiles:
                ID = profile.get('href')
                if ID not in all_profile_url:
                    all_profile_url.append(ID)

            time.sleep(10)
            driver_duckduckgo.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(30)

            try:
                next_button = driver_duckduckgo.find_element(By.CLASS_NAME, 'result--more__btn')
                next_button.click()
            except:
                break
    except:
        pass
    print('duckduckgo')
    driver_duckduckgo.close()
    return all_profile_url
