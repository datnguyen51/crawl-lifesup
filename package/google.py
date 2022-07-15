import time
import requests

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_google(options, timkiem):
    # driver google.com
    driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver.get('https://www.google.com/')
    search_google = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_google.send_keys(timkiem)
    search_google.send_keys(Keys.ENTER)

    all_profile_url = []
    all_profile_urls = []
    try:
        while True:
            time.sleep(10)
            page_source = BeautifulSoup(driver.page_source, "html.parser")

            time.sleep(10)
            profiles = page_source.find_all("a", class_="sVXRqc")

            for profile in profiles:
                profile_url = profile.get('data-pcu')
                response = requests.get(profile_url + 'cart/')
                if response.status_code == 200:
                    ID = profile.get('href')
                    if ID not in all_profile_url:
                        all_profile_url.append(ID)

            time.sleep(10)
            profiles2 = page_source.find_all("div", class_="yuRUbf")

            for profile2 in profiles2:
                href = profile2.find("a")['href']
                if href not in all_profile_urls:
                    all_profile_urls.append(href)

            time.sleep(10)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(20)

            try:
                next_button = driver.find_element(By.ID, 'pnnext')
                next_button.click()
            except:
                break
    except:
        pass
    print('google')
    driver.close()
    return all_profile_urls + all_profile_url
