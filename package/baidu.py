import time

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_url_website_with_baidu(options, timkiem):
    # driver https://www.baidu.com/
    driver_baidu = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver_baidu.get('https://www.baidu.com/')
    search_baidu = driver_baidu.find_element(By.CLASS_NAME, 's_ipt')
    search_baidu.send_keys(timkiem)
    search_baidu.send_keys(Keys.ENTER)

    all_profile_url = []
    page_number = 1
    try:
        while True:
            time.sleep(10)
            page_source = BeautifulSoup(driver_baidu.page_source, "html.parser")

            time.sleep(10)
            profiles = page_source.find_all("div", class_="result c-container xpath-log new-pmd")

            for profile in profiles:
                ID = profile.get('mu')
                if ID not in all_profile_url:
                    all_profile_url.append(ID)

            time.sleep(10)
            driver_baidu.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(30)

            try:
                next_button = driver_baidu.find_elements(By.CLASS_NAME, 'n')
                if page_number == 1:
                    if next_button[0].get_attribute('href'):
                        next_button[0].click()
                    else:
                        break
                elif (len(next_button) > 1):
                    if next_button[1].get_attribute('href'):
                        next_button[1].click()
                    else:
                        break
                else:
                    break
            except:
                break

            page_number += 1
    except:
        pass
    print('baidu')
    driver_baidu.close()
    return all_profile_url
